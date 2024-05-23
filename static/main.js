document.addEventListener("DOMContentLoaded", function() {
    // Confirmación antes de eliminar una tarea
    const deleteButtons = document.querySelectorAll(".btn-danger");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            const confirmed = confirm("¿Estás seguro de que quieres eliminar esta tarea?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    // Validación del formulario de tareas
    const form = document.querySelector("form");
    const input = document.querySelector("input[name='content']");

    form.addEventListener("submit", function(event) {
        if (input.value.trim() === "") {
            alert("La tarea no puede estar vacía");
            event.preventDefault();
        }
    });

    const completeButtons = document.querySelectorAll(".complete-task");


    completeButtons.forEach(button => {
        button.addEventListener("click", function() {
            const taskContent = this.parentElement.previousElementSibling;
            taskContent.style.textDecoration = "line-through";
        });
    });

    form.addEventListener("submit", function(event) {
        if (input.value.trim() === "") {
            alert("Task content cannot be empty!");
            event.preventDefault();
        }
    });
});
