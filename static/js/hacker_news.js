const darkModeButton = document.querySelector('.night-mode-button');

darkModeButton.addEventListener('click', () => {
    document.querySelector('body').classList.toggle('dark-mode')
    darkModeButton.classList.toggle('active');
})
