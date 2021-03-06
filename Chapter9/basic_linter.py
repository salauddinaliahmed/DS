import Stacks

class SimpleLinter:
    def __init__(self, code):
        self.code = code
        self.s = Stacks.Stack()
        self.braces = {
            '{':"}",
            '[':"]",
            '(':')',
            '<':'>'
        }
        self.code_stack = self._create_stack()

    def _create_stack(self):
        all_open_braces = list(self.braces.keys())
        all_open_braces.extend(self.braces.values())
        all_braces = [x for x in self.code if x in all_open_braces]
        print(f"All braces: {all}")
        for _ in all_braces:
            if _ in list(self.braces.keys()):
                self.s.push(_)
            
            else:
                last_brace_in_stack = self.s.pop()

                if not last_brace_in_stack:
                    print(f"No opening bracket for: {_}")
                    return

                if self.braces[last_brace_in_stack] != _:
                    print(f"No closing brace for {last_brace_in_stack}") 
                    return


        # Stack is not empty, meaning we missed a closing bracket.
        if x:=self.s.pop():
            print(f"{x} does not have a closing backet.")
            return

        print("No errors in code!")

if __name__ == "__main__":
    code = 'function lala(){var x=5; console.log("Hello World");]'
    SimpleLinter(code)
