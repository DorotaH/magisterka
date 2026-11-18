# Szablon oceny LLM

Oceń dwa fragmenty kodu Pythona prezentujące to samo zadanie. Korzystaj wyłącznie z dostarczonych fragmentów. Jeżeli widzisz ryzyko błędu wynikające ze składni, wcięć lub logiki, wskaż je ostrożnie na podstawie treści.

Dla lewej i prawej wersji podaj wynik 1–5 oraz krótkie uzasadnienie dla każdej cechy:

- czytelność
- nazewnictwo
- idiomatyczność
- utrzymywalność
- ryzyko błędu, gdzie 5 oznacza wysokie ryzyko
- ślady automatycznej modyfikacji, gdzie 5 oznacza silne ślady

Wybierz preferowaną wersję, `left` lub `right`, i uzasadnij wybór jednym zdaniem. Zwróć JSON bez otaczającego tekstu.

```json
{
  "left": {
    "readability": {"score": 1, "reason": "..."},
    "naming": {"score": 1, "reason": "..."},
    "idiomaticity": {"score": 1, "reason": "..."},
    "maintainability": {"score": 1, "reason": "..."},
    "error_risk": {"score": 1, "reason": "..."},
    "automation_traces": {"score": 1, "reason": "..."}
  },
  "right": {},
  "preference": "left",
  "reason": "..."
}
```

W polu `right` użyj tych samych sześciu kryteriów.

## Metadane rejestru

Dla każdej odpowiedzi zapisz model z pełnym identyfikatorem, parametry, powtórzenie, kierunek prezentacji, fragment, warunek, aliasy wariantów oraz pełną surową odpowiedź. Plan obejmuje co najmniej trzy powtórzenia na kolejność. Analizuj preferencję strony, powtarzalność przy odwróceniu kolejności i zależność wyboru od długości obu fragmentów. Porównanie z ludźmi obejmuje pary wspólne dla obu źródeł odpowiedzi.

### Lewa wersja

{{left_code}}

### Prawa wersja

{{right_code}}
