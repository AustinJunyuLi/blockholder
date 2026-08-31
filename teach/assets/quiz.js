/* Reusable quiz widget. Markup contract:
 *
 *   <div class="quiz">
 *     <fieldset class="quiz-q" data-answer="b">
 *       <legend>1. Question text</legend>
 *       <button data-opt="a">First option</button>
 *       <button data-opt="b">Second option</button>
 *       <p class="quiz-why" hidden>Why the answer is what it is.</p>
 *     </fieldset>
 *     ...
 *     <p class="quiz-score" hidden></p>
 *   </div>
 *
 * One click locks the question, colours the options, and shows the why.
 * When every question is answered the score line appears.
 */
(function () {
  "use strict";

  function initQuiz(quiz) {
    var questions = Array.prototype.slice.call(quiz.querySelectorAll(".quiz-q"));
    var score = quiz.querySelector(".quiz-score");
    var answered = 0;
    var correct = 0;

    if (score) {
      score.setAttribute("role", "status");
      score.setAttribute("aria-live", "polite");
    }

    questions.forEach(function (q) {
      var answer = q.getAttribute("data-answer");
      var why = q.querySelector(".quiz-why");
      var buttons = Array.prototype.slice.call(q.querySelectorAll("button[data-opt]"));
      var verdict = document.createElement("span");
      verdict.className = "quiz-verdict";
      verdict.setAttribute("role", "status");
      verdict.setAttribute("aria-live", "polite");
      verdict.setAttribute("aria-atomic", "true");
      q.insertBefore(verdict, why);

      buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          if (q.dataset.done) return;
          q.dataset.done = "1";
          answered += 1;

          buttons.forEach(function (b) {
            b.disabled = true;
            if (b.getAttribute("data-opt") === answer) b.classList.add("correct");
          });
          var isCorrect = btn.getAttribute("data-opt") === answer;
          if (isCorrect) {
            correct += 1;
          } else {
            btn.classList.add("incorrect");
          }
          verdict.textContent = isCorrect
            ? "Correct."
            : "Not quite. The highlighted option is correct.";
          if (why) why.hidden = false;

          if (score && answered === questions.length) {
            score.hidden = false;
            score.textContent =
              correct + " of " + questions.length +
              (correct === questions.length
                ? ". Recognition check complete. Close the page and explain the mechanism from memory."
                : ". Ask about the missed mechanism before the closed-page explanation.");
          }
        });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".quiz"), initQuiz);
  });
})();
