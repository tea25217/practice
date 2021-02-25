abstract class Show {
  def show: String
}

class ShowablePair[T1 <: Show, T2 <: Show](val t1: T1, val t2: T2) extends Show {
  override def show: String = "(" + t1.show + "," + t2.show + ")"
}

case class Pair[A, B](val a: A, val b: B)

class Container[+T](n: T) {
  def put[E >: T](a: E): Container[E] = new Container(a)
  def get(): T = n
}

object Challenge {
  def isSorted[E](sortedSeq: Seq[E])(ordered: (E, E) => Boolean): Boolean = {
    if (sortedSeq.length <= 1) return true
    for (i <- 0 until sortedSeq.length - 1) {
      if (!ordered(sortedSeq(i), sortedSeq(i + 1))) return false
    }
    true
  }
}

