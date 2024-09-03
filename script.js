const form = document.getElementById('dataForm');
const dataContainer = document.getElementById('dataContainer');
const clearButton = document.getElementById('clearButton');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(form);
    const dataItem = document.createElement('div');
    dataItem.className = 'data-item';

    formData.forEach((value, key) => {
        const paragraph = document.createElement('p');
        paragraph.textContent = `${key}: ${value}`;
        dataItem.appendChild(paragraph);
    });

    dataContainer.appendChild(dataItem);
    form.reset();
});

clearButton.addEventListener('click', function() {
    dataContainer.innerHTML = '';
});