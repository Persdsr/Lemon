"use strict";

new Swiper('.swiper1', {
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    mousewheel: {
        sensitivity: 1,
        eventsTarget: ".swiper1"
    },
});

new Swiper('.swiper2', {
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    mousewheel: {
        sensitivity: 1,
        eventsTarget: ".swiper1"
    },
});

const recipeBlock = document.querySelector('.recipe');
const recipeEasy = document.querySelector('.recipe__easy');
const recipeMiddle = document.querySelector('.recipe__middle');
const recipeLong = document.querySelector('.recipe__long');
const recipeItemOne = document.querySelector('.recipe__item-1');
const recipeItemTwo = document.querySelector('.recipe__item-2');
const recipeItemThree = document.querySelector('.recipe__item-3');

recipeItemOne.classList.add('active');
recipeItemTwo.classList.add('active');
recipeItemThree.classList.add('active');

recipeBlock.addEventListener("click", function(event) {
	let clicked = event.target.closest('.recipe__slozhnost');

	if (event.target.closest('.recipe__slozhnost')) {
		recipeEasy.classList.remove('active');
		recipeMiddle.classList.remove('active');
		recipeLong.classList.remove('active');

		clicked.classList.add('active');

	}

	if (recipeEasy.classList.contains('active')) {
		recipeItemOne.classList.add('active');

		recipeItemTwo.classList.remove('active');
		recipeItemThree.classList.remove('active');
	}
	if (recipeMiddle.classList.contains('active')) {
		recipeItemTwo.classList.add('active');

		recipeItemOne.classList.remove('active');
		recipeItemThree.classList.remove('active');
	}
	if (recipeLong.classList.contains('active')) {
		recipeItemThree.classList.add('active');

		recipeItemOne.classList.remove('active');
		recipeItemTwo.classList.remove('active');
	}
});