(ns ch1
  (:require [clojure.string :as s]))

(def patrol-car "パトカー")
(def taxi "タクシー")
(def pi "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")

;; 00
(defn reverse-string [str]
  (s/reverse str))

;; 01
(defn extract-string [s1]
  (s/join (take-nth 2 s1)))

;; 02
(defn join-string [s1 s2]
  (s/join (interleave s1 s2)))

