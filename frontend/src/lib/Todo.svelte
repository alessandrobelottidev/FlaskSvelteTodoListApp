<script>
    export let todo

    let clicked = false

    const handleTodo = async () => {
        clicked = true

        // Update todo server-side
        const response = await fetch(`http://localhost:5000/api/todos/${todo.id}`, {
            method: 'PUT',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                complete: !todo.complete
            })
        })

        if (response.ok) todo.complete = !todo.complete

        clicked = false
    }
</script>

<li class={todo.complete ? 'line-through' : ''} on:click={(!clicked) ? handleTodo : void(0)}>ID{todo.id} - {todo.text}</li>