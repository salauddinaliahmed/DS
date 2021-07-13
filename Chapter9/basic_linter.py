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
            if _ in list(self.braces.values()):
                self.s.push(_)
                print(self.s)
            
            else:
                last_brace_in_stack = self.s.pop()
                print(f"Last: {last_brace_in_stack}")

                if not last_brace_in_stack:
                    print(f"Closing brace is missing for: {_}")
                    return

                if last_brace_in_stack != self.braces[_]:
                    print(f"The brace {_} does not have an opening brace: {self.braces[_]}") 
                    return


        # Stack is not empty, meaning we missed a closing bracket.
        if x:=self.s.pop():
            print(f"{x} does not have a closing backet.")
            return

        print("No errors in code!")

if __name__ == "__main__":
    code = 'function lala(){var x=5; console.log("Hello World";}'
    SimpleLinter(code)
