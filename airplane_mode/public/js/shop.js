
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('filter-form');  // Select the filter form

    form.addEventListener('submit', function(event) {
        event.preventDefault();  

        // Get filter values
        const status = document.getElementById('status').value;
        const minRent = document.getElementById('min_rent').value;
        const maxRent = document.getElementById('max_rent').value;

        // Build the query parameters
        const queryParams = new URLSearchParams();

        if (status) {
            queryParams.append('status', status);
        }
        if (minRent) {
            queryParams.append('min_rent', minRent);
        }
        if (maxRent) {
            queryParams.append('max_rent', maxRent);
        }

        // Redirect the user to the filtered URL
        window.location.href = minRent || maxRent || status ?`${window.location.pathname}?${queryParams.toString()}`:window.location.pathname;
    });
});
