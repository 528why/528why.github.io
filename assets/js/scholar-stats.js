(function () {
  "use strict";
  var script = document.currentScript;
  var citation = document.getElementById("total_cit");
  if (!citation || !script) return;
  var cacheKey = "huyu-wu-scholar-stats";
  var baseline = Date.parse("2026-10-12T00:00:00Z");

  function valid(data) {
    return data && Number.isInteger(data.citedby) && data.citedby >= 0 &&
      typeof data.updated === "string" && Number.isFinite(Date.parse(data.updated));
  }

  function apply(data) {
    citation.textContent = String(data.citedby);
    var link = citation.closest("a");
    if (link) link.title = "Google Scholar citations · Updated " +
      new Date(data.updated).toLocaleDateString();
    document.querySelectorAll(".show_paper_citations").forEach(function (element) {
      var paper = (data.publications || {})[element.getAttribute("data")];
      if (paper && Number.isInteger(paper.num_citations)) {
        element.textContent = "| Citations: " + paper.num_citations;
      }
    });
  }

  try {
    var cached = JSON.parse(localStorage.getItem(cacheKey));
    if (valid(cached) && Date.parse(cached.updated) >= baseline) apply(cached);
  } catch (_) { /* Storage can be unavailable in private browsing. */ }

  fetch(script.dataset.scholarUrl, { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) throw new Error("Citation data unavailable");
      return response.json();
    })
    .then(function (data) {
      if (!valid(data) || Date.parse(data.updated) < baseline) return;
      apply(data);
      try { localStorage.setItem(cacheKey, JSON.stringify(data)); } catch (_) {}
    })
    .catch(function () { /* Keep the last successful count or the initial 125. */ });
})();
