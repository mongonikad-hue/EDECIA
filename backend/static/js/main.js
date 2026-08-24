/* ── THEME ─────────────────────────────────── */
function initTheme() {
  const saved = localStorage.getItem('edecia-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  updateToggleIcon(saved);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('edecia-theme', next);
  updateToggleIcon(next);
}

function updateToggleIcon(theme) {
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
    btn.innerHTML = theme === 'dark'
      ? '<i class="fa-solid fa-sun"></i>'
      : '<i class="fa-solid fa-moon"></i>';
  });
}

// L'initialisation du thème et les écouteurs d'événements sont gérés dans le bloc d'initialisation global à la fin du fichier.

/* ── EDITOR ─────────────────────────────────── */
const pageKey = `edecia-page-${location.pathname.split('/').pop().replace('.html', '')}`;
const editableBlocks = document.querySelectorAll('[data-edit-id]');
const editButtons = document.querySelectorAll('[data-edit-toggle]');

function loadSavedContent() {
  const saved = localStorage.getItem(pageKey);
  if (!saved) return;
  try {
    const content = JSON.parse(saved);
    editableBlocks.forEach((block) => {
      const id = block.dataset.editId;
      if (content[id]) block.innerHTML = content[id];
    });
  } catch (error) {
    console.warn('Impossible de charger le contenu enregistré', error);
  }
}

function setEditable(enabled) {
  editableBlocks.forEach((block) => {
    block.contentEditable = enabled ? 'true' : 'false';
  });
  editButtons.forEach((button) => {
    button.dataset.editState = enabled ? 'on' : 'off';
    button.textContent = enabled ? 'Enregistrer le contenu' : 'Modifier le contenu';
  });
}

function saveEditableContent() {
  const content = {};
  editableBlocks.forEach((block) => {
    content[block.dataset.editId] = block.innerHTML;
  });
  localStorage.setItem(pageKey, JSON.stringify(content));
}

function initEditor() {
  editButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const isEditing = button.dataset.editState === 'on';
      if (isEditing) saveEditableContent();
      setEditable(!isEditing);
    });
  });
}

/* ── PHONE INPUT ────────────────────────────── */
function initPhoneInput() {
  const phoneInput = document.querySelector('#phone-input');
  if (!phoneInput) return;
  window.intlTelInput(phoneInput, {
    initialCountry: 'ug',
    separateDialCode: true,
    preferredCountries: ['ug', 'cd', 'fr', 'be', 'us', 'gb'],
    utilsScript: 'https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/utils.js'
  });
}

/* ── UI INTERACTIVITY ───────────────────────── */

/* ── INIT ───────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  loadSavedContent();
  initEditor();
  initPhoneInput();
  setEditable(false);

  // Attache l'événement click à tous les boutons de changement de thème
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
    btn.addEventListener('click', toggleTheme);
  });

  /* ── CHANGE NAVBAR ON SCROLL ────────────────────────────── */
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 0);
    });
  }

  /* ── PRODUCT/PROJECT FILTER ──────────────────────────────── */
  const ProjectButtons = document.querySelectorAll('.product-filter button');
  const ProjectItems = document.querySelectorAll('.product-grid li');

  ProjectButtons.forEach(button => {
    button.addEventListener('click', () => {
      const ChosenButton = button.dataset.filter;

      ProjectButtons.forEach(btn => btn.classList.toggle('is-active', btn === button));

      ProjectItems.forEach(item => {
        const Project = item.dataset.category;
        if (ChosenButton === 'all' || ChosenButton === Project) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    });
  });
});