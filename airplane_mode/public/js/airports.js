function toggleDetails(element) {
    console.log(element)
    const airportItem = element.closest('.airport-item');
    const details = airportItem.querySelector('.airport-details');
    const arrowDown = element.querySelector('.arrow-down');
    const arrowUp = element.querySelector('.arrow-up');

    // Toggle the details visibility
    details.classList.toggle('hidden');

    // Toggle arrow direction
    arrowDown.classList.toggle('hidden');
    arrowUp.classList.toggle('hidden');
}


function fun2(element) {
    let inp = element.value
    console.log(inp)

}

