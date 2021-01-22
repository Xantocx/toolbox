const app = Vue.createApp({
    data() {
        return {
            nodes: [node1, node2]
        }
    }
})


class Rectangle {

    constructor(x, y, width, height) {
        this.x = x
        this.y = y
        this.width = width
        this.height = height
    }
}


class Node {

    constructor(rectangle, color) {
        this.rectangle = rectangle
        this.color = color
        this.zIndex = 0
    }

    get x() {
        return this.rectangle.x
    }

    set x(newVal) {
        this.rectangle.x = newVal
    }

    get y() {
        return this.rectangle.y
    }

    set y(newVal) {
        this.rectangle.y = newVal
    }

    get width() {
        return this.rectangle.width
    }

    set width(newVal) {
        this.rectangle.width = newVal
    }

    get height() {
        return this.rectangle.height
    }

    set height(newVal) {
        this.rectangle.height = newVal
    }

    get style() {
        return {
            top: this.x.toString() + "px",
            left: this.y.toString() + "px",
            height: this.height.toString() + "px",
            width: this.width.toString() + "px",
            backgroundColor: this.color,
            zIndex: this.zIndex
        }
    }

    updatePosition(delta) {
        this.x += delta.dx
        this.y += delta.dy
    }
}


const node1 = new Node(new Rectangle(10, 10, 100, 100), "green")
const node2 = new Node(new Rectangle(100, 100, 100, 100), "orange")