
// Function to handle search when the button is clicked
function searchAirport() {
    let searchInput = document.querySelector('.search-box');
    let inp = searchInput.value.trim();  // Get the trimmed input value

    if (inp) {
        // If the input is not empty, add the query parameter to the URL
        let queryParams = new URLSearchParams();
        queryParams.append("city", inp);
        window.location.href = `${window.location.pathname}?${queryParams.toString()}`;
    } else {
        // If the input is empty, reset to the base URL
        window.location.href = window.location.pathname;
    }
}

// Attach event listener to the button
document.querySelector('.search-airport-btn').addEventListener('click', function() {
    searchAirport();  // Trigger the searchAirport function on button click
});


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

