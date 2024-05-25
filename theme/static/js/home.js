document.addEventListener("DOMContentLoaded", function () {
    let index = 0;
    const items = document.querySelectorAll('.carousel-item');
    const totalItems = items.length;

    function showItem(newIndex) {
        items[index].classList.remove('active');
        index = newIndex;
        items[index].classList.add('active');
    }

    function showNextItem() {
        const newIndex = (index + 1) % totalItems;
        showItem(newIndex);
    }

    function showPrevItem() {
        const newIndex = (index - 1 + totalItems) % totalItems;
        showItem(newIndex);
    }
    document.getElementById('next').addEventListener('click', showNextItem);
    document.getElementById('prev').addEventListener('click', showPrevItem);

    setInterval(showNextItem, 4000); // Cambia la imagen cada 4 segundos
});