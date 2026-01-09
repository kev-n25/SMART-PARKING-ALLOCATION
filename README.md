# SMART-PARKING-ALLOCATION
🚗 Smart Parking Allocation using Nash Equilibrium

This project presents a smart parking recommendation system that helps users identify optimal parking spots in urban areas. It uses an interactive map to display 
parking availability near the user’s location and models parking decisions using game theory (Nash Equilibrium).

Parking spots are generated along nearby roads and categorized into zones based on distance, congestion, and cost. Each spot is evaluated using a utility 
function that balances price and congestion. The Nash equilibrium approach ensures a stable and optimal parking recommendation where no user benefits by unilaterally changing their choice.

The system visually distinguishes parking states using intuitive color coding—red for occupied spots, green for free spots, and yellow for the recommended
optimal spot. The backend is implemented using Python and Flask, while the frontend uses Leaflet.js and OpenStreetMap for real-time map interaction.

This project demonstrates the practical application of mathematical modeling and game theory in solving real-world urban mobility and parking challenges.
