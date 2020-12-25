const XlsxPopulate = require('xlsx-populate');

XlsxPopulate.fromBlankAsync().then(workbook => { // 空のワークブックを作成する。
    workbook.sheet(0).cell("A1").value("機密情報"); // A1 セルに文章を書き込む。

    // パスワード保護された Excel の書き出し
    workbook.toFileAsync("./encryption.xlsx", { password: "S3cret!" }); // パスワードを S3cret! に設定。
});