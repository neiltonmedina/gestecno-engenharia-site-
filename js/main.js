/* ==========================================================================
   Gestecno Engenharia — scripts
   Sem dependências. Sem cookies e sem analytics.
   ========================================================================== */
(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Ano atual no rodapé ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------- Sombra no topo ao rolar ---------- */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Menu hambúrguer (celular) ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("menu-principal");
  var toggleLabel = toggle ? toggle.querySelector(".visually-hidden") : null;
  var desktop = window.matchMedia("(min-width: 960px)");

  function setMenu(open, returnFocus) {
    if (!toggle || !nav) return;
    toggle.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
    if (toggleLabel) toggleLabel.textContent = open ? "Fechar menu" : "Abrir menu";
    if (!open && returnFocus) toggle.focus();
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") !== "true";
      setMenu(open);
      if (open) {
        var first = nav.querySelector("a");
        if (first) first.focus();
      }
    });

    // Fecha ao escolher um item do menu
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a") && !desktop.matches) setMenu(false);
    });

    // Fecha com Esc e devolve o foco ao botão
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setMenu(false, true);
      }
    });

    // Fecha ao clicar fora
    document.addEventListener("click", function (e) {
      if (
        toggle.getAttribute("aria-expanded") === "true" &&
        !nav.contains(e.target) &&
        !toggle.contains(e.target)
      ) {
        setMenu(false);
      }
    });

    // Ao passar para o layout desktop, reseta o estado do menu
    desktop.addEventListener("change", function () {
      setMenu(false);
    });
  }

  /* ---------- Destaque do item de menu da seção visível ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.site-nav__list a[href^="#"]'));
  if ("IntersectionObserver" in window && navLinks.length) {
    var byId = {};
    navLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = byId[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {
          navLinks.forEach(function (a) { a.classList.remove("is-active"); a.removeAttribute("aria-current"); });
          link.classList.add("is-active");
          link.setAttribute("aria-current", "true");
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(byId).forEach(function (id) {
      var section = document.getElementById(id);
      if (section) sectionObserver.observe(section);
    });
  }

  /* ---------- Animação de entrada dos blocos ---------- */
  var revealTargets = document.querySelectorAll(
    ".section__head, .about__text, .about__facts, .card, .step, .feature, .gallery__item, .contact__intro, .contact__list, .cta-band__inner"
  );
  if (!reduceMotion && "IntersectionObserver" in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          revealObserver.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    revealTargets.forEach(function (el, i) {
      el.classList.add("reveal");
      // Pequeno atraso escalonado entre itens irmãos
      var index = Array.prototype.indexOf.call(el.parentNode.children, el);
      el.style.transitionDelay = Math.min(index, 5) * 70 + "ms";
      revealObserver.observe(el);
    });
  }

  /* ---------- Galeria / lightbox ----------
     Sem JavaScript, cada foto é um link que abre a imagem diretamente. */
  var links = Array.prototype.slice.call(document.querySelectorAll(".gallery__link"));
  var box = document.getElementById("lightbox");
  if (!links.length || !box) return;

  var img = box.querySelector(".lightbox__img");
  var caption = box.querySelector(".lightbox__caption");
  var counter = box.querySelector(".lightbox__counter");
  var btnClose = box.querySelector(".lightbox__close");
  var btnPrev = box.querySelector(".lightbox__prev");
  var btnNext = box.querySelector(".lightbox__next");
  var current = 0;
  var lastFocus = null;
  var touchStartX = null;

  function show(index) {
    current = (index + links.length) % links.length;
    var link = links[current];
    var thumb = link.querySelector("img");
    img.src = link.getAttribute("href");
    img.alt = thumb ? thumb.alt : "";
    caption.textContent = link.getAttribute("data-caption") || "";
    counter.textContent = "Foto " + (current + 1) + " de " + links.length;
    // Pré-carrega a próxima foto
    var next = new Image();
    next.src = links[(current + 1) % links.length].getAttribute("href");
  }

  function open(index) {
    lastFocus = document.activeElement;
    show(index);
    box.hidden = false;
    document.body.classList.add("is-locked");
    btnClose.focus();
  }

  function close() {
    box.hidden = true;
    document.body.classList.remove("is-locked");
    img.src = "";
    if (lastFocus) lastFocus.focus();
  }

  links.forEach(function (link, i) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      open(i);
    });
  });

  btnClose.addEventListener("click", close);
  btnPrev.addEventListener("click", function () { show(current - 1); });
  btnNext.addEventListener("click", function () { show(current + 1); });

  // Clique no fundo escuro fecha
  box.addEventListener("click", function (e) {
    if (e.target === box) close();
  });

  // Teclado: Esc fecha, setas navegam, Tab fica preso dentro do lightbox
  box.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { e.preventDefault(); close(); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); show(current - 1); }
    else if (e.key === "ArrowRight") { e.preventDefault(); show(current + 1); }
    else if (e.key === "Tab") {
      var focusables = [btnClose, btnPrev, btnNext];
      var idx = focusables.indexOf(document.activeElement);
      e.preventDefault();
      var nextIdx = e.shiftKey ? (idx <= 0 ? focusables.length - 1 : idx - 1) : (idx + 1) % focusables.length;
      focusables[nextIdx].focus();
    }
  });

  // Gesto de deslizar no celular
  box.addEventListener("touchstart", function (e) {
    touchStartX = e.changedTouches[0].clientX;
  }, { passive: true });
  box.addEventListener("touchend", function (e) {
    if (touchStartX === null) return;
    var dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
    touchStartX = null;
  }, { passive: true });
})();
