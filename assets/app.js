"use strict";

const app = document.getElementById("app");
const countEl = document.getElementById("site-count");
let DATA = null;
let filter = "all";

const FILTERS = [
  ["all", "すべて"],
  ["stock", "ストック"],
  ["doing", "試作中"],
  ["done", "試作済み・見送り"],
];

function esc(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function renderList() {
  const posts = DATA.posts.filter((p) => filter === "all" || p.status === filter);
  countEl.textContent = "全" + DATA.site.count + "件";
  let html = '<div class="filters">';
  for (const [key, label] of FILTERS) {
    const n = key === "all" ? DATA.posts.length : DATA.posts.filter((p) => p.status === key).length;
    html += '<button data-filter="' + key + '"' + (filter === key ? ' class="active"' : "") + ">" + label + "（" + n + "）</button>";
  }
  html += '</div><div class="tiles">';
  for (const p of posts) {
    html += '<a class="tile" href="#post/' + esc(p.slug) + '">'
      + '<span class="meta"><time>' + esc(p.date) + '</time><span class="badge ' + esc(p.status) + '">' + esc(p.status_label) + "</span></span>"
      + "<h2>" + esc(p.title) + "</h2>"
      + "<p>" + esc(p.summary) + "</p></a>";
  }
  html += "</div>";
  app.innerHTML = html;
  app.querySelectorAll("[data-filter]").forEach((b) => {
    b.addEventListener("click", () => { filter = b.dataset.filter; renderList(); });
  });
}

function renderPost(slug) {
  const p = DATA.posts.find((x) => x.slug === slug);
  if (!p) { renderList(); return; }
  countEl.textContent = "全" + DATA.site.count + "件";
  let html = '<a class="back-link" href="#">← 一覧へ戻る</a>'
    + '<article class="article"><div class="meta"><time>' + esc(p.date) + '</time><span class="badge ' + esc(p.status) + '">' + esc(p.status_label) + "</span></div>"
    + "<h1>" + esc(p.title) + "</h1>"
    + '<div class="body">' + p.html + "</div>";
  if (p.source) {
    html += '<a class="source-link" href="' + esc(p.source) + '" target="_blank" rel="noopener">元の情報を見る</a>';
  }
  html += "</article>";
  app.innerHTML = html;
  window.scrollTo(0, 0);
}

function route() {
  if (!DATA) return;
  const m = location.hash.match(/^#post\/(.+)$/);
  if (m) renderPost(decodeURIComponent(m[1]));
  else renderList();
}

window.addEventListener("hashchange", route);

fetch("data.json")
  .then((r) => r.json())
  .then((d) => { DATA = d; route(); })
  .catch((e) => { app.innerHTML = '<p class="loading">data.json を読み込めませんでした。</p>'; });
