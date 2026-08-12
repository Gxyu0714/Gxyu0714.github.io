// EN / 中文 toggle. Persists preference in localStorage.
const LANG_KEY = "site-lang";
const DEFAULT_LANG = "en";

const getStoredLang = () => {
  const stored = localStorage.getItem(LANG_KEY);
  return stored === "zh" || stored === "en" ? stored : DEFAULT_LANG;
};

const applyLang = (lang) => {
  const next = lang === "zh" ? "zh" : "en";
  document.documentElement.setAttribute("data-lang", next);
  document.documentElement.setAttribute("lang", next === "zh" ? "zh-CN" : "en");
  localStorage.setItem(LANG_KEY, next);

  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    const dict = window.SITE_I18N && window.SITE_I18N[next];
    if (dict && dict[key]) {
      el.textContent = dict[key];
    }
  });

  const toggle = document.getElementById("lang-toggle-label");
  if (toggle && window.SITE_I18N && window.SITE_I18N[next]) {
    toggle.textContent = window.SITE_I18N[next].lang_toggle;
  }
};

const toggleLang = () => {
  applyLang(getStoredLang() === "en" ? "zh" : "en");
};

const initLang = () => {
  applyLang(getStoredLang());
  document.addEventListener("DOMContentLoaded", () => {
    applyLang(getStoredLang());
    const btn = document.getElementById("lang-toggle");
    if (btn) {
      btn.addEventListener("click", toggleLang);
    }
  });
};

initLang();
