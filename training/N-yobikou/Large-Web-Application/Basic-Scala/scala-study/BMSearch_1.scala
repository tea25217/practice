//解答例のコードを見てスキップテーブル作成部分の書き方を取り込み

object BMSearch_1 extends App {
  val text = "カワカドカドカドドワンゴカドカドンゴドワドワンゴドワカワカドンゴドワ".toSeq
  val pattern = "ドワンゴ".toSeq
  val matchIndexes = search(text, pattern)

  def search(text: Seq[Char], pattern: Seq[Char]): Seq[Int] = {
    val skipTable: Map[Char, Int] = getSkipNums(pattern)  //文字をキー、その文字が出現した際にずらす数を値に持つ連想配列
    println("skipTable: " + skipTable)
    val offsetAfterMatch = getOffsetOfMatchedLetter(pattern)  //マッチした場合にずらす数
    println("offsetAfterMatch: " + offsetAfterMatch)
    val lastIndex = text.length - pattern.length
    var matchIndexes = Seq[Int]()
    var i = 0

    while (i <= lastIndex) {
      val partText = text.slice(i, i + pattern.length)
      println("partText: " + partText)
      val (isMatch, shift) = matchTextAndGetNumToShift(partText, pattern, skipTable, offsetAfterMatch)  //isMatch: Boolean, shift: Int
      if (isMatch) matchIndexes = matchIndexes :+ i
      i = i + shift
    }

    matchIndexes
  }

  def getSkipNums(pattern: Seq[Char]): Map[Char, Int] = {
    return pattern.map(s => (s -> (pattern.reverse.indexOf(s)))).toMap
  }

  def getOffsetOfMatchedLetter(pattern: Seq[Char]): Int = {
    var num = pattern.length

    for (i <- pattern.length - 2 to 0 by -1 if pattern.last != pattern(i)){
      num = pattern.length - i -1
      return num
    }
    num
  }

  def matchTextAndGetNumToShift(partText: Seq[Char], pattern: Seq[Char], skipTable: Map[Char, Int], offsetAfterMatch: Int): (Boolean, Int) = {
    var isMatch = false
    var shift = pattern.length

    for (i <- pattern.length - 1 to 0 by -1) {
      if (partText(i) != pattern(i)) {
        shift = skipTable.getOrElse(partText(i), shift)
        return (isMatch, shift)
      }
    }
    isMatch = true
    shift = offsetAfterMatch  //マッチ後、同じ文字がある場合への対応

    (isMatch, shift)
  }

  println(s"出現場所: ${matchIndexes}")
}