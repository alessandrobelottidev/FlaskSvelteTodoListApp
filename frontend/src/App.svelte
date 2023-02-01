<script>
  import Navbar from "./lib/Navbar.svelte"
  import Todo from "./lib/Todo.svelte"
  import AddTodo from "./lib/AddTodo.svelte"

  import { onMount } from "svelte/internal"

  import { todos } from "./stores/store"

  // Fetch todos from REST api on mount
  onMount(async () => {
    const response = await fetch("http://localhost:5000/api/todos")
    const data = await response.json()
    todos.set(data)
  })
</script>

<main>
  <Navbar />
  <ul class="p-4 pt-20 pb-16 overflow-y-auto overflow-x-none h-screen">
    {#each $todos as todo}
      <Todo {todo} />
      <div class="divider my-0"></div>
    {/each}
  </ul>
  <AddTodo />
</main>
