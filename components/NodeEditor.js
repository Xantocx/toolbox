app.component("node-editor", {

    props: {
        nodes: {
            type: Array,
            required: true
        }
    },

    template:
        /*html*/
        `<div 
            class="node-view fill-screen"
            @mousemove="updatePosition"
            @mouseup.left="stopDragging">

            <node 
                v-for="node in nodes" 
                :node="node" 
                @start-dragging="startDragging">
            </node>
        </div>`,

    data() {
        return {
            isDragging: false,
            draggedNode: null,
            lastPosition: null
        }
    },

    methods: {
        startDragging(node) {
            if (this.draggedNode !== null) {
                this.draggedNode.zIndex = 0
            }

            node.zIndex = 1
            this.draggedNode = node
            this.isDragging = true
        },
        updatePosition(event) {
            const x = event.clientY
            const y = event.clientX

            if (this.isDragging && this.lastPosition !== null) {
                const delta = { dx: x - this.lastPosition.x, dy: y - this.lastPosition.y }
                this.draggedNode.updatePosition(delta)
            }

            this.lastPosition = { x: x, y: y }
        },
        stopDragging() {
            this.isDragging = false
        }
    }
})