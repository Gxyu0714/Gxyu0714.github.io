// Enable smoother News scrolling + hide fade when at bottom.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".news-scroll--fade").forEach((wrap) => {
    const inner = wrap.querySelector(".news-scroll__inner");
    if (!inner) return;

    const update = () => {
      const atBottom = inner.scrollTop + inner.clientHeight >= inner.scrollHeight - 2;
      wrap.classList.toggle("is-at-bottom", atBottom);
    };

    inner.addEventListener("scroll", update, { passive: true });
    update();
  });
});
