# O Conclave Tenebroso: Zumbi Contra a Sombra do Império

**Conclave Tenebroso** is a roguelike game featuring a unique twist on chess. You play as Zumbi, an ex-slave who has escaped the clutches of the Shadow Empire and returned to reclaim what they have stolen from their people.

## Game Objective

The objective of the game is to eliminate all the shadows, ultimately defeating the Shadow Empire. However, be cautious, as if Zumbi is defeated, the game is lost.

## Controls

- Use the arrow keys to move Zumbi.
- Zumbi can only move in the four cardinal directions (up, down, left, right).
- Zumbi moves one cell per frame.
- If an enemy shadow moves onto the same cell as Zumbi, Zumbi is instantly defeated.
- By moving over enemy shadows, Zumbi can eliminate them.

## Shadow Types

The Shadow Empire consists of various types of shadows, each with their own movement patterns:

- **Pawn** (♙): Moves in the four cardinal directions, just like Zumbi.
- **Rook** (♖): Moves in the four cardinal directions, but can move twice in a single turn.
- **Bishop** (♗): Moves diagonally in the four diagonal directions (up-left, up-right, down-left, down-right).
- **Knight** (♘): Moves in a unique "L" shape, combining the movement of a Pawn and a Bishop. It moves one step orthogonally (up, down, left, right) and then one step diagonally.
- **King** (♔): Moves in any direction (orthogonal and diagonal) but only one cell at a time.
- **Queen** (♕): Combines the movement of a King and a Rook. It can move in any direction (orthogonal and diagonal) and can move twice in a single turn.

Make sure to have the `getch` Python plugin installed to play the game.
