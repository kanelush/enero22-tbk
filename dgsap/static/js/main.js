// const { default: gsap } = require("gsap/gsap-core");

// console.log("hello world")

// gsap.registerPlugin(ScrollTrigger);



// console.log("imported")

gsap.from('.navbar', { duration: 0.5, y: '-100%', ease: 'power2.in'})
gsap.from('.module', { duration: 1, y: '-100%', ease: 'power2.in'})
// gsap.from('.boxes', { duration: 1, opacity: 0, delay: 1, stagger: 0.6})
// console.log("imported")


// gsap.to(".square",{
//  x: 1000,
//  duration:6,
//  scrollTrigger: {
//      trigger: ".square",
//      start: "top 80%",
//      end: "top 30%",
//      scrub: 4,
//      toggleActions: "restart none none none",
//      pin: ".square",
//      markers: {
//          startColor: "purple",
//          endColor: "fuchsia",
//          fontSize: "3rem",
//      },
//  }

// })
gsap.registerPlugin(ScrollTrigger)

let container = document.getElementById("container");

gsap.to(container, {
  x: () => -(container.scrollWidth - document.documentElement.clientWidth) + "px",
  ease: "none",
  scrollTrigger: {
    trigger: container,
    invalidateOnRefresh: true,
    pin: true,
    scrub: 1,
    end: () => "+=" + container.offsetWidth
  }
})

//NAVBAR

document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
  
      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {
  
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
  
          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
  
        });
      });
    }
  
  });