object NumberFormatter {

  def format(number: Int): String = {
    val minus = if (number < 0) "-"  else ""
    val reversed: String = number.abs.toString.reverse
    val indexedSeq: Seq[(Char, Int)] = reversed.zipWithIndex
    val nestedSeq: Seq[Seq[Char]] = indexedSeq.map(
      (t) => if ((t._2 % 3 == 2) && !(t._2 + 1 == indexedSeq.length)) {
        Seq(t._1, ',')
      } else {
        Seq(t._1)
      })
    minus + nestedSeq.flatten.reverse.mkString
  }

}
