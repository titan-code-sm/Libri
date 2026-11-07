# Come usare questa cartella con Munder Difflin

1. Scompatta la cartella `sirena-blu` dove preferisci (per esempio in Documenti).
2. Inizializzala come repository Git (Munder Difflin lavora con cartelle registrate):
   ```
   cd sirena-blu
   git init && git add . && git commit -m "Inizio serie Sirena Blu"
   ```
3. Apri Munder Difflin e, nella procedura iniziale, registra la cartella `sirena-blu` come progetto.
4. Crea quattro agenti con Claude Code e chiamali: `scrittore`, `editor`, `prompt`, `marketing`.
5. Come prima istruzione a ciascuno, scrivi:
   > Leggi CLAUDE.md e agenti/<nome>.md: sono le tue istruzioni di ruolo.
6. A Michael scrivi:
   > Leggi CLAUDE.md e agenti/michael.md: sei il capo di questo ufficio.
7. Primo compito da provare, rivolto a Michael:
   > Fai scrivere il libro 2, "Sirena Blu e la bua di Biscotto", e fammelo rivedere prima di andare avanti.

## Consigli
- Approva sempre la storia prima di far partire prompt e marketing: è previsto dal flusso di Michael.
- I punti `[VERIFICA MAT]` sono le informazioni di soccorso da controllare tu: sei l'esperto.
- Munder Difflin è ancora un prototipo: se un agente non riceve i messaggi, dagli l'istruzione direttamente nel suo terminale.
- Le illustrazioni vanno generate a parte, incollando i prompt di `prompt-illustrazioni/` nel tuo generatore di immagini.
