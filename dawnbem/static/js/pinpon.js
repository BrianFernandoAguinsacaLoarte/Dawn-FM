const lightThemeButton = document.getElementById('lightTheme');
const darkThemeButton = document.getElementById('darkTheme');
const body = document.body;

lightThemeButton.addEventListener('click', () => {
    body.classList.remove('dark-mode');
});

darkThemeButton.addEventListener('click', () => {
    body.classList.add('dark-mode');
});

