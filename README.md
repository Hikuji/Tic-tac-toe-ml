# Tic-Tac-Toe-ML

Konsolowa gra w kółko i krzyżyk przeciwko prostemu, uczącemu się AI. Gracz wybiera
znak `X` albo `O`, a komputer zapisuje wyniki swoich decyzji i wykorzystuje je
w kolejnych partiach. Projekt jest obecnie grywalny, ale jego rozwój jest
wstrzymany. Ta dokumentacja opisuje bieżące działanie oraz pomysły na wypadek
powrotu do projektu w przyszłości.

## Spis treści

- [Wymagania i uruchomienie](#wymagania-i-uruchomienie)
- [Instrukcja dla gracza](#instrukcja-dla-gracza)
- [Jak działa aplikacja](#jak-działa-aplikacja)
- [Funkcje i klasy](#funkcje-i-klasy)
- [Jak działa AI](#jak-działa-ai)
- [Dane zapisywane przez grę](#dane-zapisywane-przez-grę)
- [Stan projektu i plany](#stan-projektu-i-plany)

## Wymagania i uruchomienie

- Python **3.12 lub nowszy**. Kod używa składni f-stringów obsługiwanej od
  Pythona 3.12.
- Terminal: PowerShell, Wiersz polecenia lub terminal systemu Linux/macOS.
- Zależności z pliku `requirements.txt`: `colorama` i `platformdirs`.

Uruchomienie w Windows PowerShell, z katalogu głównego projektu:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

Jeśli PowerShell blokuje aktywację środowiska, można jednorazowo zezwolić na
uruchomienie skryptu tylko w bieżącym oknie:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

W Wierszu polecenia (cmd.exe) aktywacja wygląda tak:

```bat
.venv\Scripts\activate.bat
```

Na Linuxie/macOS utwórz i aktywuj środowisko poleceniami:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Po aktywacji środowiska grę uruchamia się z katalogu projektu poleceniem
`python main.py`. Przy kolejnym uruchomieniu nie trzeba ponownie instalować
zależności: wystarczy aktywować `.venv` i uruchomić program. Zakończenie
środowiska w terminalu: `deactivate`.

## Instrukcja dla gracza

### Menu

Po uruchomieniu pojawia się ekran powitalny. Naciśnij Enter, a następnie
wybierz numer:

1. **Play** — rozpoczęcie partii.
2. **Rules** — zasady wyświetlane w grze.
3. **Statistics** — podsumowanie zapisanych partii (w obecnym interfejsie
   etykieta jest wyświetlana jako `base.statistics`).
4. **Exit** — prośba o potwierdzenie wyjścia.

Wpisz numer i naciśnij Enter. Po obejrzeniu zasad, statystyk lub wyniku naciśnij
Enter, aby wrócić do menu. W menu wyjścia `Y` kończy grę, a `N` lub `n` wraca
do menu. Wybór `y` małymi literami nie jest obsługiwany przez obecną wersję.

**Ustawienia nie są na razie dostępne z poziomu gry.** Program tworzy i
wczytuje wewnętrzny plik ustawień, ale nie ma opcji ani ekranu menu, w którym
gracz mógłby je zmieniać.

### Przebieg partii

1. Wybierz `Play`.
2. Wpisz `X` albo `O`. Wielkość liter nie ma znaczenia.
3. `X` zawsze wykonuje pierwszy ruch. Jeśli wybierzesz `O`, pierwszy rusza się
   komputer.
4. Przy swojej turze wpisz numer wolnego pola od `1` do `9`, a następnie
   naciśnij Enter.
5. Zajęte pola oraz numery spoza zakresu są odrzucane; program poprosi o
   poprawny ruch.
6. Partia kończy się, gdy ktoś ułoży trzy swoje znaki w wierszu, kolumnie lub
   po przekątnej, albo gdy zapełni się plansza i nie ma zwycięzcy.

Numeracja pól:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Kolory planszy: wolne pola są żółte, ruchy gracza zielone, ruchy AI niebieskie,
a zwycięska trójka jest wyróżniana na czerwono. W terminalu, który nie obsługuje
kolorów ANSI, kolory mogą być niewidoczne.

Na ekranie wyniku remis jest oznaczony jako `DRAW!`; zwycięstwo gracza i AI
wyświetlane jest z odpowiednim symbolem. Statystyki obejmują łączną liczbę
partii, zwycięstwa gracza, zwycięstwa AI i remisy.

## Jak działa aplikacja

### Przepływ programu

Punktem wejścia jest `main.py`:

1. `setup()` przygotowuje katalogi i pliki danych, wczytuje pamięć AI oraz
   statystyki.
2. Program pokazuje ekran powitalny i przechodzi do menu.
3. Po wybraniu gry tworzy pustą planszę i pyta o symbol gracza.
4. Sterowanie przechodzi naprzemiennie między graczem i AI. Po każdym ruchu
   sprawdzane są warunki końca gry.
5. Przy końcu partii program aktualizuje pamięć AI, zapisuje statystyki i
   wyświetla wynik.

`main()` używa nazwanych stanów (`WELCOME`, `MENU`, `GAME`, `PLAYER`, `AI`,
`END`, `RULES`, `STATS`, `CONFIRM_EXIT`, `EXIT`), aby kierować przepływem bez
osobnego okna graficznego. Plansza jest listą dziewięciu pól. W `Board` druga
lista przechowuje ich zawartość (`1`–`9`, `X` albo `O`), a pierwsza — kolory
używane przy renderowaniu.

### Funkcje i klasy

#### `main.py`

- `main()` — inicjalizuje dane, obsługuje menu, tworzy planszę i prowadzi całą
  partię. Przechowuje również historię stanów planszy i ruchów AI potrzebną do
  późniejszej aktualizacji jego pamięci.

#### `game/data/base.py`

- `Board.__init__()` — tworzy nową planszę z polami ponumerowanymi od 1 do 9
  i domyślnymi kolorami.
- `Board.schema` — właściwość budująca tekstową, sformatowaną planszę na
  podstawie bieżącej zawartości i kolorów.

Plik definiuje też ścieżki danych użytkownika (`data_dir`, `settings_dir`,
`ai_memory_dir`, `settings_file`, `stats_file`, `memory`), listy katalogów
i plików do utworzenia oraz wspólne słowniki `settings` i `statistics`.

#### `game/functions/game.py`

- `get_symbol(error)` — pyta gracza o `X` lub `O`, zamienia wpis na wielkie
  litery i ponawia pytanie przy niepoprawnej odpowiedzi. Parametr `error`
  włącza komunikat o błędnym wyborze.
- `check_board(board)` — sprawdza osiem możliwych linii zwycięstwa. Zwraca
  `(symbol, pola_zwycięskiej_linii)`, `("draw", None)` dla remisu albo `None`,
  jeśli gra trwa.
- `color_board(board_colors, combo)` — zaznacza pola zwycięskiej linii; nic
  nie robi, jeżeli nie ma takiej linii (np. przy remisie).

#### `game/functions/display.py`

- `clear()` — czyści terminal (`cls` w Windows, `clear` w pozostałych systemach).
- `line(multiplier, style)` — drukuje ozdobną linię złożoną ze znaków `=`.
- `box(text, text_style, box_style)` — drukuje tekst w obramowaniu; zawiera
  wewnętrzną funkcję `empty_line()`, która rysuje puste wiersze ramki.
- `welcome()` — wyświetla ekran powitalny i czeka na Enter.
- `menu()` — drukuje opcje menu.
- `stats()` — wyświetla bieżące statystyki i czeka na Enter.
- `confirm_exit()` — wyświetla pytanie o potwierdzenie wyjścia.
- `exit_game()` — wyświetla pożegnanie i czeka na Enter.
- `rules()` — wyświetla zasady gry zapisane w interfejsie i czeka na Enter.
- `board(board)` — drukuje przekazaną planszę w terminalu.
- `game_start()` — wyświetla ekran rozpoczęcia partii; w obecnym przepływie
  gry nie jest wywoływana.
- `win(boardd, winner, player_symbol, name)` — wyświetla planszę końcową i
  komunikat o zwycięzcy albo remisie.
- `flush_input()` — opróżnia bufor klawiatury, aby wcześniej wpisane znaki nie
  trafiały do kolejnego pytania. Na Windows używa `msvcrt`, a poza nim
  `termios`.

#### `game/functions/data.py`

- `create_required()` — tworzy katalogi danych użytkownika, jeśli ich nie ma.
- `create_stats_file()` — tworzy początkowy plik statystyk z zerowymi licznikami,
  ale nie nadpisuje już istniejącego pliku.
- `create_settings_file()` — tworzy domyślny plik ustawień, jeśli jeszcze nie
  istnieje.
- `create_memory_file()` — tworzy pusty plik pamięci AI, jeśli go brakuje.
- `get_settings()` — wczytuje ustawienia JSON do `base.settings`.
- `save_settings(settings)` — zapisuje podany słownik ustawień; funkcja
  istnieje, ale nie jest wywoływana przez dostępne menu gry.
- `setup()` — przygotowuje katalogi i pliki, wczytuje pamięć AI przez `init()`,
  statystyki oraz ustawienia.
- `load_stats()` — wczytuje JSON statystyk do `base.statistics`.
- `save_stats(result, player)` — aktualizuje licznik zwycięstw gracza, AI
  albo remisów oraz łączną liczbę partii, a następnie zapisuje plik.

#### `game/ai/core.py`

- `convert(board)` — zamienia planszę na dziewięcioznakowy wzorzec: zachowuje
  `X` i `O`, a puste pola zapisuje jako kropki.
- `count_moves(position)` — liczy zajęte pola we wzorcu. Funkcja pomocnicza,
  obecnie niewykorzystywana w głównym przepływie.
- `get_symmetries(patern, orig_move)` — tworzy obroty i odbicia planszy oraz
  przenosi indeks ruchu do odpowiadających im pozycji. Dzięki temu wiedza
  może być współdzielona dla symetrycznych układów. `patern` jest tak
  zapisanym parametrem w kodzie.
- `init()` — wczytuje JSON pamięci AI do globalnego słownika `games`.
- `save_to_file()` — zapisuje słownik `games` do pliku pamięci AI.
- `move(board)` — wybiera ruch AI. Dla nowego układu inicjuje jego punktację
  i wybiera losowe wolne pole; dla znanego wzorca próbuje najlepszej ocenionej
  decyzji, a w razie potrzeby eksploruje niepróbowane pola.
- `save_game(data, board)` — po partii przyznaje punkty decyzjom AI, uwzględnia
  wynik i historię ruchów, zmniejsza wagę wcześniejszych ruchów współczynnikiem
  `0.7`, aktualizuje symetryczne układy i zapisuje pamięć. Parametr `board`
  jest obecnie niewykorzystywany.

#### Pozostałe pliki

- `requirements.txt` — przypięte wersje zależności: `colorama` do kolorów
  terminala i `platformdirs` do wyznaczania katalogu danych użytkownika.
- `.gitignore` — wyklucza lokalne środowisko `.venv` i katalogi `__pycache__`.
- `LICENSE` — licencja BSD 3-Clause.
- `sandbox.py` — mały skrypt testowy, który drukuje planszę; nie uruchamia
  pełnej gry. Właściwym poleceniem do startu jest `python main.py`.
- `game/ai/__init__.py`, `game/data/__init__.py`,
  `game/functions/__init__.py` — pliki pakietów Pythona; obecnie nie zawierają
  dodatkowej logiki.

## Jak działa AI

To proste, lokalne uczenie przez punktowanie decyzji, a nie sieć neuronowa ani
solver gwarantujący optymalną grę. Nie ma połączenia z internetem ani usługi
zewnętrznej.

1. Plansza jest kodowana jako tekst, np. `X...O....`; kropka oznacza puste pole.
2. Przed każdym ruchem AI zapisywany jest wzorzec planszy i wybrany indeks pola
   (`0`–`8`).
3. Dla znanego wzorca AI korzysta z dziewięciu ocen ruchów. Dodatnia ocena jest
   preferowana; gdy brak dodatniej, losuje spośród jeszcze nieocenionych ruchów.
   Jeśli wszystkie ruchy mają już ocenę ujemną, wybiera najwyżej oceniony
   dostępny ruch.
4. Po partii wynik jest zamieniany na nagrodę: porażka AI `-10`, remis `+2`,
   zwycięstwo AI `+10`. Nagrody są dodawane do decyzji wstecz, z mnożnikiem
   `0.7` dla kolejnych wcześniejszych ruchów.
5. Te same informacje trafiają do odbić i obrotów planszy, żeby AI mogło
   wykorzystać doświadczenie także dla równoważnych układów.

Pamięć jest współdzielona między uruchomieniami. AI nie uczy się w trakcie
osobnego procesu treningowego: dostaje informację o wyniku dopiero po
zakończeniu partii. Ponieważ wybór może być losowy, a system punktacji jest
prosty, komputer może wykonywać słabe ruchy i nie gwarantuje, że zawsze wygra
albo zagra bezbłędnie.

## Dane zapisywane przez grę

`platformdirs` wybiera katalog danych użytkownika; pliki nie są zapisywane
w katalogu projektu. Typowe lokalizacje:

- Windows: `%LOCALAPPDATA%\Hikuji\TicTacToeML`
- Linux: `~/.local/share/TicTacToeML`
- macOS: `~/Library/Application Support/TicTacToeML`

W tym katalogu gra używa:

- `stats.json` — liczniki rozegranych partii, wygranych gracza, wygranych AI
  i remisów.
- `ai_memory\memory.json` (na Windows; odpowiednio `ai_memory/memory.json`
  na innych systemach) — oceny ruchów dla poznanych wzorców planszy.
- `settings\settings.json` (na Windows; odpowiednio
  `settings/settings.json` na innych systemach) — plik jest tworzony i
  wczytywany przez program. Domyślne ustawienia zawierają m.in. nazwę AI i
  opcję numeracji planszy, ale obecnie nie ma menu do ich zmiany.

Usunięcie lub przeniesienie katalogu danych oznacza utratę zapisanych statystyk
i wyuczonej pamięci. Przed ręczną edycją plików JSON warto wykonać ich kopię
zapasową.

## Stan projektu i plany

Projekt jest obecnie odłożony i grywalny w aktualnej postaci. Jeśli wrócę do
niego z nowym pomysłem, planuję rozważyć:

- **Menu ustawień** — udostępnienie opcji konfiguracyjnych w grze. W kodzie
  istnieje już obsługa pliku ustawień, ale gracz nie może obecnie zmieniać ich
  przez menu.
- **Język polski** — przygotowanie polskiej wersji interfejsu i zasad, najlepiej
  jako opcji językowej w ustawieniach.
- **Osobny plik do automatycznego uczenia AI** — narzędzie, które pozwoli
  trenować AI automatycznie, bez ręcznego rozgrywania każdej partii.
- **Testy automatyczne** — w szczególności sprawdzenie warunków zwycięstwa,
  ruchów AI, zapisu pamięci i statystyk.

Pamięć AI można wyczyścić ręcznie, usuwając plik `memory.json` z katalogu
danych. Nie planuję dodawać osobnej funkcji czyszczenia tej pamięci do gry.

*<small>Tekst wygenerowany przez AI</small>