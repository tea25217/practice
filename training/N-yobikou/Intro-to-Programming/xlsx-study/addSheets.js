const XlsxPopulate = require('xlsx-populate');

// 空のワークブックを作成する。
XlsxPopulate.fromBlankAsync().then(workbook => {

    // `Sheet5` という名前のシートを最後に追加する。
    const sheet5 = workbook.addSheet('Sheet5'); // -> Sheet1 Sheet5

    // `Sheet2` という名前のシートを 1番目 に追加する。(番号は 0 始まり)
    const sheet2 = workbook.addSheet('Sheet2', 1); // -> Sheet1 Sheet2 Sheet5

    // `Sheet3` という名前のシートを `Sheet5` の前に追加する。
    const sheet3 = workbook.addSheet('Sheet3', 'Sheet5'); // -> Sheet1 Sheet2 Sheet3 Sheet5

    // シートオブジェクト 'Sheet5' の変数がすでにある場合は、この変数を使って 'Sheet5' の前に `Sheet4` を追加することもできます。
    // `Sheet4` という名前のシートを `Sheet5` の前に追加する。
    const sheet4 = workbook.addSheet('Sheet4', sheet5); // -> Sheet1 Sheet2 Sheet3 Sheet4 Sheet5

    // Excel ファイルの書き出し。
    return workbook.toFileAsync("./sheetTest.xlsx");
});