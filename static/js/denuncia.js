// Aguarda o carregamento do DOM
document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Manipulação do formulário
    const denunciaForm = document.getElementById('denunciaForm');
    if (denunciaForm) {
        denunciaForm.addEventListener('submit', function(e) {
            // Se você quiser que o Django processe o formulário, 
            // NÃO use e.preventDefault() a menos que vá usar Ajax.
            alert('Enviando denúncia... Aguarde a confirmação.');
        });
    }

    // 2. Feedback visual do upload (ID do Django: id_foto)
    const inputFotos = document.getElementById('id_foto');
    if (inputFotos) {
        inputFotos.addEventListener('change', function(e) {
            const files = e.target.files;
            const uploadArea = document.querySelector('.upload-label p');
            if (files.length > 0 && uploadArea) {
                uploadArea.textContent = `${files.length} arquivo(s) selecionado(s)`;
            }
        });
    }

    // 3. Data máxima (ID do Django: id_data_ocorrencia)
    const inputData = document.getElementById('id_data_ocorrencia');
    if (inputData) {
        inputData.max = new Date().toISOString().split('T')[0];
    }

    // 4. Função showList (Protegida)
    const listView = document.getElementById('listView');
    if (listView) {
        // Se precisar chamar essa função via botão:
        window.showList = function() {
            listView.classList.remove('hidden');
        };
    }
});