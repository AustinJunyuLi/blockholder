(function () {
  "use strict";

  var lab = document.querySelector(".signal-lab");
  if (!lab) return;

  var kappa = lab.querySelector("#signal-kappa");
  var out = lab.querySelector("#signal-kappa-out");
  var read = lab.querySelector("#signal-read");
  var buttons = Array.prototype.slice.call(lab.querySelectorAll("button[data-signal-x]"));
  var prior = parseFloat(lab.getAttribute("data-prior"));
  if (!(prior >= 0 && prior <= 1)) prior = 0.5;
  var x = 1;

  function pNo(total, k) {
    if (total === -1 || total === 1) return k / 2;
    if (total === 0) return 1 - k;
    return 0;
  }

  function pYes(total, k) {
    if (total === 1) return 1 - k;
    if (total === 0 || total === 2) return k / 2;
    return 0;
  }

  function engagementPosterior(noLikelihood, yesLikelihood, engagementPrior) {
    var noMass = (1 - engagementPrior) * noLikelihood;
    var yesMass = engagementPrior * yesLikelihood;
    return noMass + yesMass ? yesMass / (noMass + yesMass) : engagementPrior;
  }

  console.assert(
    Math.abs(engagementPosterior(0.15, 0.70, 0.50) - 0.8235294117647058) < 1e-12,
    "Default posterior check failed"
  );
  console.assert(
    Math.abs(engagementPosterior(0.15, 0.70, 0.20) - 0.5384615384615384) < 1e-12,
    "Non-default prior check failed"
  );

  function draw() {
    var k = parseFloat(kappa.value);
    var no = pNo(x, k);
    var yes = pYes(x, k);
    var noMass = (1 - prior) * no;
    var yesMass = prior * yes;
    var posterior = engagementPosterior(no, yes, prior);
    out.value = k.toFixed(2);
    buttons.forEach(function (button) {
      button.setAttribute("aria-pressed", String(parseInt(button.getAttribute("data-signal-x"), 10) === x));
    });
    var verdict = no === 0 ? "certain: engager" : (yes === 0 ? "certain: no engager" : "ambiguous");
    read.innerHTML = "Prior engagement chance = " + prior.toFixed(3) + ". For total order " +
      (x > 0 ? "+" : "") + x + ", weighted mass without engagement = " +
      noMass.toFixed(3) + ", and with engagement = " + yesMass.toFixed(3) +
      ". Therefore P(engagement | order) = <b>" + posterior.toFixed(3) +
      "</b>. <b>" + verdict + "</b>.";
  }

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      x = parseInt(button.getAttribute("data-signal-x"), 10);
      buttons.forEach(function (b) { b.classList.toggle("sel", b === button); });
      draw();
    });
  });
  kappa.addEventListener("input", draw);
  draw();
})();
