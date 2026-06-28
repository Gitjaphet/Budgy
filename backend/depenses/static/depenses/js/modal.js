// Ouvrir un modal
function openModal(id) {
    document.getElementById(id).classList.add('active');
}

// Fermer un modal
function closeModal(id) {
    document.getElementById(id).classList.remove('active');
}

// Fermer en cliquant dehors
document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', function(e) {
        if (e.target === this) {
            this.classList.remove('active');
        }
    });
});

// Ouvrir le modal supprimer avec les bonnes infos
function openDeleteModal(id, titre) {
    document.getElementById('delete-titre').textContent = titre;
    document.getElementById('form-delete').action = '/depenses/' + id + '/delete/';
    openModal('modal-delete');
}

// Ouvrir le modal modifier
function openEditModal(id) {
    window.location.href = '/depenses/' + id + '/edit/';
}


function loadEditForm(id) {
    document.getElementById('form-edit').action = '/depenses/' + id + '/edit/';
    
    fetch('/depenses/' + id + '/json/')
        .then(response => response.json())
        .then(data => {
            document.querySelector('#form-edit input[name="titre"]').value = data.titre;
            document.querySelector('#form-edit input[name="montant"]').value = data.montant;
            document.querySelector('#form-edit select[name="categorie"]').value = data.categorie;
            document.querySelector('#form-edit textarea[name="description"]').value = data.description;
        });
}