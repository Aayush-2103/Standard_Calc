// Function to append numbers to the display
function appendNumber(number) {
    document.getElementById('display').value += number;
}

// Function to append operators to the display
function appendOperator(operator) {
    document.getElementById('display').value += operator;
}

// Function to clear the display
function clearDisplay() {
    document.getElementById('display').value = '';
}

// Function to calculate the result
function calculate() {
    const expression = document.getElementById('display').value;
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression: expression }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('display').value = data.result;

        // Save the result in local storage for recent calculations
        saveRecentCalculation(expression + ' = ' + data.result);
        displayRecentCalculations();
    })
    .catch(error => {
        document.getElementById('display').value = 'Error';
    });
}

// Function to save recent calculations in local storage
function saveRecentCalculation(calculation) {
    let recentCalculations = JSON.parse(localStorage.getItem('recentCalculations')) || [];
    recentCalculations.unshift(calculation);  // Add to the beginning
    if (recentCalculations.length > 5) {
        recentCalculations.pop();  // Keep only the last 5 entries
    }
    localStorage.setItem('recentCalculations', JSON.stringify(recentCalculations));
}

// Function to display recent calculations
function displayRecentCalculations() {
    const recentCalculations = JSON.parse(localStorage.getItem('recentCalculations')) || [];
    const recentList = document.getElementById('recent-calculations');
    recentList.innerHTML = '';  // Clear the list
    recentCalculations.forEach(calculation => {
        const listItem = document.createElement('li');
        listItem.textContent = calculation;
        recentList.appendChild(listItem);
    });
}

// Display recent calculations on page load
document.addEventListener('DOMContentLoaded', displayRecentCalculations);
