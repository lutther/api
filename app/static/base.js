const navT = document.querySelector('.burger');
const navLi = document.querySelectorAll('.nav_item');

navT.addEventListener('click', () => {
	document.body.classList.toggle('nav-open');
});

navLi.forEach(link => {
	link.addEventListener('click', () => {
		document.body.classList.remove('nav-open');
	})
});