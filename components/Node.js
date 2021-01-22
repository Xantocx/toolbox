app.component("node", {

    props: {
        node: {
            type: Node,
            required: true
        }
    },

    emmits: ["start-dragging"],

    template:
        /*html*/
        `<div 
        class="node" 
        :style="style"
        @mousedown.left="startDragging">
        </div>`,

    methods: {
        startDragging() {
            this.$emit("start-dragging", this.node)
        }
    },

    computed: {
        style() {
            return this.node.style
        }
    }
})
