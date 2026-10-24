# AI Learn tic-tac-toe

## Stan projektu

Projekt jest obecnie na wczesnym etapie rozwoju i ma charakter szkicu funkcjonalności, a nie jeszcze pełnej gry z AI.

### Co jest już zrobione
- przygotowana jest struktura katalogów projektu:
  - `game/` z logiką gry i wyświetlaniem,
  - `AI/` przeznaczona na komponent uczenia maszynowego,
  - `main.py` jako punkt wejścia aplikacji,
- dodano podstawowe funkcje pomocnicze w `game/functions/game.py`:
  - `get_symbol()` — wybór symbolu gracza (`X` lub `O`),
  - `get_move()` — pobieranie ruchu od gracza i walidacja pola,
- dodano funkcje wyświetlania i obsługi konsoli w `game/functions/display.py`:
  - czyszczenie ekranu,
  - ekran powitalny,
  - proste wyświetlanie planszy,
- przygotowana jest też baza danych wizualnej planszy w `game/data/base.py` z definicją kolorów i układu pól,
- w `requirements.txt` dodano zależność `colorama`.

### Ogólny opis projektu
Celem projektu jest stworzenie gry w kółko i krzyżyk, w której komputer będzie się uczył stylu gry użytkownika i dostosowywał swoje ruchy do jego zachowania. Obecnie repozytorium zawiera tylko fundamenty architektury i podstawowe elementy interakcji z konsolą, ale nie jest jeszcze w pełni działającą aplikacją.

*<small>opis wygenerowany przez AI</small>