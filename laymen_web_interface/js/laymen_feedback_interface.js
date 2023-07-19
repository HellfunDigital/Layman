```javascript
// Laymen Feedback Interface

// Feedback Data Schema
var FeedbackDataSchema = {
    "username": "",
    "feedback": ""
};

// DOM Element ID
var feedbackForm = document.getElementById('feedbackForm');

// Message Name
var feedbackReceived = 'Feedback received. Thank you for your input!';

// Function to submit user feedback
function submitFeedback() {
    var feedbackData = Object.create(FeedbackDataSchema);
    feedbackData.username = feedbackForm.elements.namedItem('username').value;
    feedbackData.feedback = feedbackForm.elements.namedItem('feedback').value;

    // Send feedback data to server
    fetch('/submitFeedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(feedbackData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(feedbackReceived);
            feedbackForm.reset();
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Event listener for feedback form submission
feedbackForm.addEventListener('submit', function(event) {
    event.preventDefault();
    submitFeedback();
});
```