function bookTicket() {
    console.log("Booking ticket...");
    
    const flightName = document.getElementById("flight_name").value;
    const passengerName = document.getElementById("passenger_name").value;
    const csrfToken = document.getElementById("csrf").value;
    console.log(csrfToken)
    fetch('/api/method/airplane_mode.api.create_ticket', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Frappe-CSRF-Token': csrfToken
        },
        body: JSON.stringify({
            flight_name: flightName,
            passenger_name: passengerName
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert("Ticket booked successfully!");
           let id;
           if(id) clearTimeout(id)

            id = setTimeout(()=>{
                window.location.href ="http://development.localhost:8000/airports"
            },1000)
        } else {
            alert("Failed to book ticket. Please try again.");
        }
    })
    .catch(error => console.error('Error:', error));
}
