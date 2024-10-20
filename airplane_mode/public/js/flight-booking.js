function bookTicket() {
 
    
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
            console.log(data.passenger,data,"hello from line 22")
            const formBookingContainer = document.querySelector(".booking-form")
            const bookedTickedStatus = document.querySelector(".booked-ticket-container")
            const ticketDetailsContainer = document.querySelector(".ticket-details")
                 ticketDetailsContainer.innerHTML = ""
            let  ticketDetails = document.createElement("p")
                  ticketDetails.innerHTML = `Hi ${data?.message?.passenger}, your ticket is booked successfully on ${data?.message?.departure_date}.Thank you for Choosing us! 😊`
                  formBookingContainer.style.display = "none"
                  bookedTickedStatus.style.display = "block"
                  ticketDetailsContainer.append(ticketDetails)
            
           let id;
           if(id) clearTimeout(id)

            id = setTimeout(()=>{
                formBookingContainer.style.display = "block"
                bookedTickedStatus.style.display = "none"
                
            },10000)
        } else {
            alert("Failed to book ticket. Please try again.");
        }
    })
    .catch(error => console.error('Error:', error));
}
