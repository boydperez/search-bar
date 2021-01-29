var users;

$(document).ready(() => {

	$("#query-field").on('input', () => {
		var username = $("#query-field").val();

		var xhr = new XMLHttpRequest();

		xhr.open('GET', `${document.location}getdata\?username=${username}`, true);

		xhr.onload = function() {
			if (this.status == 200) {
				users = JSON.parse(this.responseText);

				// Flask endpoint /getdata returns 'NO_ARGS' 
				// if input field is left empty
				if (users.usernames == 'NO_ARGS' ) {

				} 
				// Check if the value <Array> of the key 'usernames' is empty
				else if (users.usernames.length) {
					var text = '';
					users.usernames.forEach(user => {
						text += `<li>${user}</li>`;	
					});
				} 
				// Execute if usernames query is null
				else {
					text = "<li>No results found</li>";	
				}

				// Clear older usernames
				$('#show').empty();
				$("#show").append(text);
				// Add bootstrap class for list
				$("#show li").addClass("list-group-item");
			}
		}; 
		// Send XMLHttpRequest
		xhr.send();
	});
});
