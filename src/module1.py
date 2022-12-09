from typing import Dict
from dataclasses import dataclass
from dataclasses import field


@dataclass
class Example:
    """
    Container for a example with name, unique id and content dictionary
    """

    name: str
    uuid: int
    content: Dict[str, int] = field(default_factory=dict)

    def get_content(self, key: str):
        return self.content.get(key)


if __name__ == "__main__":
    data = {
        "first": 13123,
        "second": 3333,
        "third": 33333,
        "fourth": 31351,
        "fifth": 31351,
    }
    example = Example("this", 2343, data)
    print(example)
