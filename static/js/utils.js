const darkModeButton = document.querySelector('.night-mode-button');

if (localStorage.darkMode === 'true') {
    document.querySelector('body').classList.toggle('dark-mode')
    darkModeButton.classList.toggle('active');
}

darkModeButton.addEventListener('click', () => {
    const darkModeValue = localStorage.darkMode === 'true' ? 'false' : 'true'
    localStorage.setItem('darkMode', darkModeValue)
    document.querySelector('body').classList.toggle('dark-mode')
    darkModeButton.classList.toggle('active');
})
