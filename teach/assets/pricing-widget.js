/* The pricing lab. Chains lesson 2's pooled Bayes update into lesson 3's price
 * fixed point, so one observed order produces one price.
 *
 * Markup contract:
 *
 *   <div class="widget pricing-lab"
 *        data-prior="0.5" data-ev="100" data-dv="4"
 *        data-m0="6" data-dm="10" data-k="5" data-sbar="129" data-sigma="20">
 *     <input type="range" id="price-kappa"> <output id="price-kappa-out">
 *     <button data-price-x="1"> ... </button>
 *     <svg id="price-plot"></svg>
 *     <p class="readout" id="price-read"></p>
 *   </div>
 *
 * The engager buys one unit, the non-engager submits nothing, and noise is the
 * ternary mark of lesson 2. The value posterior is held fixed on purpose: this
 * lab isolates the engagement channel.
 */
(function () {
  "use strict";

  var lab = document.querySelector(".pricing-lab");
  if (!lab) return;

  function num(name, fallback) {
    var raw = parseFloat(lab.getAttribute("data-" + name));
    return isFinite(raw) ? raw : fallback;
  }

  var PRIOR = num("prior", 0.5);
  var EV = num("ev", 100);
  var DV = num("dv", 4);
  var M0 = num("m0", 6);
  var DM = num("dm", 10);
  var KCOST = num("k", 5);
  var SBAR = num("sbar", 129);
  var SIGMA = num("sigma", 20);

  /* Standard normal CDF, Abramowitz and Stegun 26.2.17, error below 7.5e-8. */
  function Phi(x) {
    var b1 = 0.319381530, b2 = -0.356563782, b3 = 1.781477937;
    var b4 = -1.821255978, b5 = 1.330274429, c = 0.2316419;
    var ax = Math.abs(x);
    var t = 1 / (1 + c * ax);
    var d = 0.398942280401433 * Math.exp(-ax * ax / 2);
    var poly = b1 + t * (b2 + t * (b3 + t * (b4 + t * b5)));
    var y = 1 - d * t * poly;
    return x >= 0 ? y : 1 - y;
  }

  /* Lesson 2's pooled likelihoods, noise size normalised to one. */
  function likeEngage(x, k) {
    if (x === 1) return 1 - k;
    if (x === 0 || x === 2) return k / 2;
    return 0;
  }
  function likeQuiet(x, k) {
    if (x === 0) return 1 - k;
    if (x === -1 || x === 1) return k / 2;
    return 0;
  }
  function posterior(x, k, prior) {
    var yes = prior * likeEngage(x, k);
    var no = (1 - prior) * likeQuiet(x, k);
    return yes + no ? yes / (yes + no) : prior;
  }

  /* Entry probability and the pricing map P -> ybar + mbar * odds of entry. */
  function entry(P, mbar) {
    return 1 - Phi((P + KCOST + mbar - SBAR) / SIGMA);
  }
  function priceMap(P, ybar, mbar) {
    var p = entry(P, mbar);
    return ybar + mbar * p / (1 - p);
  }

  /* The map is non-increasing in P and the identity is strictly increasing, so
   * g = map - P is strictly decreasing and bisection finds its one root. */
  function solvePrice(pi) {
    var ybar = EV + pi * DV;
    var mbar = M0 + pi * DM;
    var g = function (P) { return priceMap(P, ybar, mbar) - P; };
    var lo = ybar, hi = ybar + 1;
    var guard = 0;
    while (g(hi) > 0 && guard < 200) { hi = ybar + (hi - ybar) * 2; guard += 1; }
    for (var i = 0; i < 200; i += 1) {
      var mid = (lo + hi) / 2;
      if (g(mid) > 0) lo = mid; else hi = mid;
    }
    var P = (lo + hi) / 2;
    return { pi: pi, ybar: ybar, mbar: mbar, P: P, p: entry(P, mbar) };
  }

  /* Self-checks on the lesson's worked calibration. */
  console.assert(Math.abs(Phi(0) - 0.5) < 1e-8, "Phi(0) check failed");
  console.assert(Math.abs(posterior(1, 0.30, 0.5) - 0.8235294117647058) < 1e-12,
    "Lesson 2 posterior at kappa 0.30 failed");
  console.assert(Math.abs(posterior(1, 0.60, 0.5) - 0.5714285714285714) < 1e-12,
    "Lesson 2 posterior at kappa 0.60 failed");
  console.assert(Math.abs(solvePrice(0.5).P - 113) < 1e-6,
    "Baseline fixed point should be exactly 113");
  console.assert(Math.abs(solvePrice(0.5).p - 0.5) < 1e-7,
    "Baseline entry probability should be one half");
  console.assert(Math.abs(solvePrice(posterior(1, 0.30, 0.5)).P - 113.6932) < 5e-5,
    "Lesson's quoted price at kappa 0.30 failed");
  console.assert(Math.abs(solvePrice(posterior(1, 0.60, 0.5)).P - 113.1871) < 5e-5,
    "Lesson's quoted price at kappa 0.60 failed");

  var kappaIn = lab.querySelector("#price-kappa");
  var kappaOut = lab.querySelector("#price-kappa-out");
  var read = lab.querySelector("#price-read");
  var plot = lab.querySelector("#price-plot");
  var buttons = Array.prototype.slice.call(lab.querySelectorAll("button[data-price-x]"));
  var x = 1;

  var BASE = solvePrice(PRIOR);
  var W = 640, Hgt = 336, ML = 56, MR = 16, MT = 38, MB = 40;

  function drawPlot(sol) {
    var half = 12;
    var p0 = sol.P - half, p1 = sol.P + half;
    var v0 = sol.P - half, v1 = sol.P + half;
    var sx = function (P) { return ML + (P - p0) / (p1 - p0) * (W - ML - MR); };
    var sy = function (v) { return Hgt - MB - (v - v0) / (v1 - v0) * (Hgt - MT - MB); };

    var d = "", started = false;
    for (var i = 0; i <= 240; i += 1) {
      var P = p0 + (p1 - p0) * i / 240;
      var v = priceMap(P, sol.ybar, sol.mbar);
      if (v < v0 - 60 || v > v1 + 60) { started = false; continue; }
      var cy = Math.max(MT - 8, Math.min(Hgt - MB + 8, sy(v)));
      d += (started ? "L" : "M") + sx(P).toFixed(1) + " " + cy.toFixed(1) + " ";
      started = true;
    }

    /* x ticks at both ends and the crossing; y ticks only at the top and the
     * crossing, so the bottom-left corner does not stack two labels. */
    var ticks = "";
    [p0, sol.P, p1].forEach(function (P) {
      ticks += '<line x1="' + sx(P).toFixed(1) + '" y1="' + (Hgt - MB) +
        '" x2="' + sx(P).toFixed(1) + '" y2="' + (Hgt - MB + 5) +
        '" stroke="#5a5a52" stroke-width="1"/>' +
        '<text x="' + sx(P).toFixed(1) + '" y="' + (Hgt - MB + 20) +
        '" text-anchor="middle" font-size="12" fill="#5a5a52">' + P.toFixed(1) + "</text>";
    });
    [sol.P, v1].forEach(function (v) {
      ticks += '<line x1="' + (ML - 5) + '" y1="' + sy(v).toFixed(1) +
        '" x2="' + ML + '" y2="' + sy(v).toFixed(1) +
        '" stroke="#5a5a52" stroke-width="1"/>' +
        '<text x="' + (ML - 9) + '" y="' + (sy(v) + 4).toFixed(1) +
        '" text-anchor="end" font-size="12" fill="#5a5a52">' + v.toFixed(1) + "</text>";
    });

    plot.setAttribute("viewBox", "0 0 " + W + " " + Hgt);
    plot.setAttribute("role", "img");
    plot.setAttribute("aria-label",
      "The pricing map slopes down and the forty five degree line slopes up. They cross once, at " +
      sol.P.toFixed(2) + ".");
    plot.innerHTML =
      '<line x1="' + ML + '" y1="' + MT + '" x2="' + ML + '" y2="' + (Hgt - MB) +
        '" stroke="#e3e0d5" stroke-width="1"/>' +
      '<line x1="' + ML + '" y1="' + (Hgt - MB) + '" x2="' + (W - MR) + '" y2="' + (Hgt - MB) +
        '" stroke="#e3e0d5" stroke-width="1"/>' +
      ticks +
      '<line x1="' + sx(p0) + '" y1="' + sy(v0) + '" x2="' + sx(p1) + '" y2="' + sy(v1) +
        '" stroke="#6f6413" stroke-width="1.5" stroke-dasharray="5 4"/>' +
      '<path d="' + d + '" fill="none" stroke="#4477aa" stroke-width="2"/>' +
      '<circle cx="' + sx(sol.P).toFixed(1) + '" cy="' + sy(sol.P).toFixed(1) +
        '" r="5" fill="#147765"/>' +
      '<line x1="' + ML + '" y1="14" x2="' + (ML + 22) +
        '" y2="14" stroke="#4477aa" stroke-width="2"/>' +
      '<text x="' + (ML + 28) + '" y="18" font-size="12" fill="#4477aa">pricing map</text>' +
      '<line x1="' + (ML + 128) + '" y1="14" x2="' + (ML + 150) +
        '" y2="14" stroke="#6f6413" stroke-width="1.5" stroke-dasharray="5 4"/>' +
      '<text x="' + (ML + 156) + '" y="18" font-size="12" fill="#6f6413">price equals itself</text>' +
      '<text x="' + ((ML + W - MR) / 2) + '" y="' + (Hgt - 6) +
        '" text-anchor="middle" font-size="12" fill="#5a5a52">candidate price P</text>';
  }

  function draw() {
    var k = parseFloat(kappaIn.value);
    var pi = posterior(x, k, PRIOR);
    var sol = solvePrice(pi);
    var impact = sol.P - BASE.P;
    kappaOut.value = k.toFixed(2);
    buttons.forEach(function (b) {
      var on = parseInt(b.getAttribute("data-price-x"), 10) === x;
      b.classList.toggle("sel", on);
      b.setAttribute("aria-pressed", String(on));
    });
    drawPlot(sol);
    read.innerHTML =
      "Order " + (x > 0 ? "+" : "") + x + " at &kappa; = " + k.toFixed(2) +
      " gives engagement posterior &pi; = <b>" + sol.pi.toFixed(4) + "</b>. Then " +
      "y&#772; = " + sol.ybar.toFixed(3) + " and m&#772; = " + sol.mbar.toFixed(3) +
      ", so the price solves to <b>P* = " + sol.P.toFixed(4) + "</b> with entry chance " +
      sol.p.toFixed(4) + ". Against the no-order price " + BASE.P.toFixed(4) +
      ", the price impact of this order is <b>" + (impact >= 0 ? "+" : "") +
      impact.toFixed(4) + "</b>.";
  }

  buttons.forEach(function (b) {
    b.addEventListener("click", function () {
      x = parseInt(b.getAttribute("data-price-x"), 10);
      draw();
    });
  });
  kappaIn.addEventListener("input", draw);
  draw();
})();
