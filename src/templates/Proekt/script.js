function openPopup(id) {
    document.getElementById('popup' + id).style.display = 'block';
    clearProducts(id);
    fetchProducts(id);
}

function closePopup(id) {
    document.getElementById('popup' + id).style.display = 'none';
}

function clearProducts(id) {
    const productsContainer = document.getElementById('products' + id);
    productsContainer.innerHTML = '';
}

function fetchProducts(id) {
    // Здесь вы можете получить данные о продуктах для конкретного попапа
    // Например, путем отправки запроса на сервер

    // Пример данных о продуктах
    const products = [
        { name: 'Product ' + id + ' 1', image: 'product' + id + '_1.jpg', price: '10' },
        { name: 'Product ' + id + ' 2', image: 'product' + id + '_2.jpg', price: '15' },
        { name: 'Product ' + id + ' 3', image: 'product' + id + '_3.jpg', price: '20' },
        { name: 'Product ' + id + ' 4', image: 'product' + id + '_4.jpg', price: '15' },
        { name: 'Product ' + id + ' 5', image: 'product' + id + '_5.jpg', price: '15' },
        { name: 'Product ' + id + ' 6', image: 'product' + id + '_6.jpg', price: '10' },
        { name: 'Product ' + id + ' 7', image: 'product' + id + '_7.jpg', price: '15' },
        { name: 'Product ' + id + ' 8', image: 'product' + id + '_8.jpg', price: '20' },
        { name: 'Product ' + id + ' 9', image: 'product' + id + '_9.jpg', price: '15' },
        { name: 'Product ' + id + ' 10', image: 'product' + id + '_10.jpg', price: '15' },
    ];

    const productsContainer = document.getElementById('products' + id);

    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product');

        const imageElement = document.createElement('img');
        imageElement.src = product.image;
        productElement.appendChild(imageElement);

        const priceButton = document.createElement('button');
        priceButton.textContent = 'Price: ' + product.price;
        priceButton.addEventListener('click', () => {
            alert(`You clicked on the price button for ${product.name}`);
        });
        productElement.appendChild(priceButton);

        productsContainer.appendChild(productElement);
    });
}





