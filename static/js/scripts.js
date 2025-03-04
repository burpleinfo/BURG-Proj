// scripts.js

// Function to handle search form submission
document.querySelector('.hero form')?.addEventListener('submit', function (e) {
    e.preventDefault();
    const location = document.querySelector('input[name="location"]').value;
    const startDate = document.querySelector('input[name="start_date"]').value;
    const endDate = document.querySelector('input[name="end_date"]').value;
    alert(`Searching for vehicles in ${location} from ${startDate} to ${endDate}`);
});

// Function to dynamically load featured vehicles
function loadFeaturedVehicles() {
    const vehicleList = document.querySelector('.vehicle-list');
    if (vehicleList) {
        const vehicles = [
            { name: "Tata Ace", image: "https://truckcdn.cardekho.com/in/tata/ace-diesel/tata-ace-diesel.jpg", price: "$50/day" },
            { name: "Force Traveller", image: "https://i.ytimg.com/vi/6HwNZ6Ahmp0/maxresdefault.jpg", price: "$40/day" },
            { name: "Eicher Starline", image: "https://i.ytimg.com/vi/jJqtYxliNMw/maxresdefault.jpg", price: "$70/day" },
        ];

        vehicles.forEach(vehicle => {
            const vehicleCard = document.createElement('div');
            vehicleCard.className = 'vehicle-card';
            vehicleCard.innerHTML = `
                <img src="${vehicle.image}" alt="${vehicle.name}">
                <h3>${vehicle.name}</h3>
                <p>${vehicle.price}</p>
            `;
            vehicleList.appendChild(vehicleCard);
        });
    }
}

// Cost Calculator
function calculateCost() {
    const vehicleType = document.getElementById("vehicle-type").value;
    const days = document.getElementById("days").value;
    const cost = vehicleType * days;
    document.getElementById("cost-result").innerText = `Total Cost: $${cost}`;
}

// Load featured vehicles on page load
window.onload = loadFeaturedVehicles;