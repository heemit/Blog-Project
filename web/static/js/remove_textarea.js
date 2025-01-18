document.addEventListener('DOMContentLoaded', function() {
    // Wait for the DOM to fully load
    
    // Target the textarea element by its ID
    var textareaElement = document.querySelector("#id_featured_text");

    // Check if the textarea exists and remove it
    if (textareaElement) {
        textareaElement.remove();
    }
    
    // Ensure GrapeJS editor is visible
    var grapeJSContainer = document.querySelector("#gjs-container-featured_text");
    if (grapeJSContainer) {
        grapeJSContainer.style.display = 'block';  // Ensure GrapeJS is visible
    }
});
