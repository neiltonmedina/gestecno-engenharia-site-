/* ==========================================================================
   Gestecno Engenharia — scripts
   Sem dependências. Sem cookies e sem analytics.
   ========================================================================== */
(function () {
  "use strict";

  document.documentElement.classList.remove("no-js");

  /* ---------- Ano atual no rodapé ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

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

  /* ---------- Galeria / lightbox ----------
     Implementado na próxima etapa. Sem JavaScript, cada foto da galeria
     é um link que abre a imagem ampliada diretamente. */
})();
