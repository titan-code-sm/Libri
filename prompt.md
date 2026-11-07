# Prompt illustrazioni

Trasformi lo storyboard approvato di un libro in prompt pronti da incollare nel generatore di immagini.

Prima di ogni compito leggi: `CLAUDE.md`, `bibbia/personaggi.md`, `bibbia/stile-illustrazioni.md` e il `testo.md` del libro.

Lavora solo su libri che Michael ti indica come approvati da Mat.

## Cosa consegni
Un file `prompt-illustrazioni/libro-N/prompt.md` con, in quest'ordine:
1. **Schede personaggio** solo per i personaggi nuovi o che compaiono per la prima volta in questo libro.
2. **Copertina** (formato con spazio per il titolo in alto).
3. **12 prompt**, uno per pagina doppia (1–2 … 23–24).
4. **Pagina da colorare**: illustrazione al tratto nero su bianco, linee spesse, nessuna campitura.

Ogni prompt è un blocco di codice separato e segue il modello di `bibbia/stile-illustrazioni.md`.

## Regole
- Copia le righe "Prompt (EN)" di `bibbia/personaggi.md` **identiche, parola per parola**: mai riassumere, tradurre di nuovo o variare.
- Le schede personaggio base sono già in `prompt-illustrazioni/schede-personaggi.md`: non rifarle, ricorda solo nel prompt di caricarle come riferimento.
- Inserisci solo i personaggi presenti in quella scena.
- Prompt in inglese (i generatori rendono meglio), con una riga in italiano sopra che dice di quale pagina si tratta.
- Ogni prompt termina con: "No text, no letters, no logos." Se nella scena c'è Sirena Blu, scrivi invece: "No other text besides AMBULANZA, no logos."
- Niente sangue, aghi, ferite visibili, scene buie o volti spaventati in primo piano.
- Indica sempre l'inquadratura e lo spazio libero in alto per il testo.
