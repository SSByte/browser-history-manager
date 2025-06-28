class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self):
        self.current = None

    def visit(self, url):
        new_node = Node(url)
        if self.current:
            # Remove forward history
            self.current.next = None
            new_node.prev = self.current
        self.current = new_node
        print(f"Visited: {url}")

    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Moved back to: {self.current.url}")
        else:
            print("No previous page.")

    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Moved forward to: {self.current.url}")
        else:
            print("No next page.")

    def current_page(self):
        if self.current:
            print(f"Current page: {self.current.url}")
        else:
            print("No page loaded.")


def main():
    history = BrowserHistory()
    while True:
        print("\n📜 Browser History Menu")
        print("1. Visit new URL")
        print("2. Back")
        print("3. Forward")
        print("4. Current Page")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            url = input("Enter URL to visit: ")
            history.visit(url)
        elif choice == '2':
            history.back()
        elif choice == '3':
            history.forward()
        elif choice == '4':
            history.current_page()
        elif choice == '5':
            print("Exiting browser history manager.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
