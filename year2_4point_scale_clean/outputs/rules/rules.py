def findDecision(obj): #obj[0]: Kỹ năng mềm, obj[1]: Đại số tuyến tính, obj[2]: Giải tích 1, obj[3]: Tin học đại cương, obj[4]: Vật lý điện từ, obj[5]: Giải tích 2, obj[6]: Lập trình nâng cao, obj[7]: Môn tự chọn 1, obj[8]: Thiết kế Web, obj[9]: Toán rời rạc, obj[10]: Cấu trúc dữ liệu và giải thuật, obj[11]: Kiến trúc và tổ chức máy tính, obj[12]: Lập trình hướng đối tượng, obj[13]: Xác suất thống kê, obj[14]: Hệ điều hành, obj[15]: Công nghệ Java, obj[16]: Cơ sở dữ liệu, obj[17]: Phân tích thiết kế thuật toán
	# {"feature": "C\u01a1 s\u1edf d\u1eef li\u1ec7u", "instances": 614, "metric_value": 1.8524, "depth": 1}
	if obj[16] == 'B':
		# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 230, "metric_value": 1.6888, "depth": 2}
		if obj[11] == 'C':
			# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 75, "metric_value": 1.5058, "depth": 3}
			if obj[0] == 'B':
				# {"feature": "H\u1ec7 \u0111i\u1ec1u h\u00e0nh", "instances": 38, "metric_value": 1.5574, "depth": 4}
				if obj[14] == 'C':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 18, "metric_value": 1.2516, "depth": 5}
					if obj[10] == 'C':
						return 'Khá'
					elif obj[10] == 'B':
						return 'Khá'
					elif obj[10] == 'A':
						return 'Giỏi'
					elif obj[10] == 'D':
						return 'Khá'
					else: return 'Khá'
				elif obj[14] == 'B':
					# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 8, "metric_value": 1.5613, "depth": 5}
					if obj[17] == 'B':
						return 'Giỏi'
					elif obj[17] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[14] == 'A':
					# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[8] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[8] == 'B':
						return 'Giỏi'
					elif obj[8] == 'A':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[14] == 'D':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[10] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[10] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[14] == 'F':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[0] == 'C':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 24, "metric_value": 1.1432, "depth": 4}
				if obj[17] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'C':
						return 'Khá'
					elif obj[3] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[3] == 'D':
						return 'Khá'
					else: return 'Khá'
				elif obj[17] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[1] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'C':
						return 'Giỏi'
					else: return 'Chưa Xếp Loại'
				elif obj[17] == 'C':
					return 'Khá'
				elif obj[17] == 'D':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[0] == 'A':
				# {"feature": "H\u1ec7 \u0111i\u1ec1u h\u00e0nh", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[14] == 'A':
					return 'Giỏi'
				elif obj[14] == 'C':
					return 'Chưa Xếp Loại'
				elif obj[14] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Giỏi'
			elif obj[0] == 'D':
				# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[10] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'D':
						return 'Khá'
					elif obj[1] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[10] == 'D':
					return 'Khá'
				elif obj[10] == 'C':
					return 'Khá'
				else: return 'Khá'
			else: return 'Khá'
		elif obj[11] == 'B':
			# {"feature": "To\u00e1n r\u1eddi r\u1ea1c", "instances": 64, "metric_value": 1.5415, "depth": 3}
			if obj[9] == 'B':
				# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 1", "instances": 27, "metric_value": 1.3516, "depth": 4}
				if obj[7] == 'B':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 15, "metric_value": 1.3996, "depth": 5}
					if obj[4] == 'A':
						return 'Giỏi'
					elif obj[4] == 'B':
						return 'Khá'
					elif obj[4] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[7] == 'A':
					return 'Giỏi'
				elif obj[7] == 'C':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[3] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[3] == 'A':
						return 'Giỏi'
					else: return 'Giỏi'
				else: return 'Giỏi'
			elif obj[9] == 'C':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 23, "metric_value": 0.9123, "depth": 4}
				if obj[0] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[1] == 'C':
						return 'Khá'
					elif obj[1] == 'A':
						return 'Khá'
					elif obj[1] == 'D':
						return 'Khá'
					elif obj[1] == 'B':
						return 'Khá'
					else: return 'Khá'
				elif obj[0] == 'C':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[10] == 'B':
						return 'Khá'
					elif obj[10] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[0] == 'D':
					return 'Khá'
				elif obj[0] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'B':
						return 'Khá'
					else: return 'Khá'
				else: return 'Khá'
			elif obj[9] == 'A':
				# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 12, "metric_value": 1.2075, "depth": 4}
				if obj[6] == 'A':
					return 'Giỏi'
				elif obj[6] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'B':
						return 'Giỏi'
					elif obj[1] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[6] == 'C':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'A':
						return 'Xuất sắc'
					elif obj[0] == 'B':
						return 'Giỏi'
					else: return 'Xuất sắc'
				elif obj[6] == 'D':
					return 'Khá'
				else: return 'Giỏi'
			elif obj[9] == 'D':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'D':
					return 'Chưa Xếp Loại'
				elif obj[0] == 'B':
					return 'Giỏi'
				else: return 'Chưa Xếp Loại'
			else: return 'Khá'
		elif obj[11] == 'D':
			# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 64, "metric_value": 1.1665, "depth": 3}
			if obj[0] == 'B':
				# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 31, "metric_value": 1.2604, "depth": 4}
				if obj[6] == 'C':
					# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[17] == 'B':
						return 'Khá'
					elif obj[17] == 'C':
						return 'Khá'
					elif obj[17] == 'A':
						return 'Khá'
					elif obj[17] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[6] == 'D':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[6] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 6, "metric_value": 1.4591, "depth": 5}
					if obj[2] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'D':
						return 'Khá'
					elif obj[2] == 'A':
						return 'Giỏi'
					else: return 'Chưa Xếp Loại'
				elif obj[6] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1] == 'B':
						return 'Khá'
					elif obj[1] == 'C':
						return 'Giỏi'
					elif obj[1] == 'D':
						return 'Khá'
					else: return 'Khá'
				else: return 'Khá'
			elif obj[0] == 'C':
				# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 24, "metric_value": 0.995, "depth": 4}
				if obj[8] == 'C':
					# {"feature": "C\u00f4ng ngh\u1ec7 Java", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[15] == 'A':
						return 'Khá'
					elif obj[15] == 'C':
						return 'Khá'
					elif obj[15] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[8] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[5] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[8] == 'B':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10] == 'C':
						return 'Khá'
					elif obj[10] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[10] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[8] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'C':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[8] == 'F':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[0] == 'D':
				return 'Chưa Xếp Loại'
			elif obj[0] == 'A':
				return 'Khá'
			else: return 'Chưa Xếp Loại'
		elif obj[11] == 'A':
			# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 26, "metric_value": 1.6342, "depth": 3}
			if obj[17] == 'A':
				# {"feature": "H\u1ec7 \u0111i\u1ec1u h\u00e0nh", "instances": 18, "metric_value": 1.4153, "depth": 4}
				if obj[14] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 16, "metric_value": 1.1982, "depth": 5}
					if obj[1] == 'A':
						return 'Xuất sắc'
					elif obj[1] == 'C':
						return 'Giỏi'
					elif obj[1] == 'B':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[14] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Giỏi'
			elif obj[17] == 'B':
				# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[8] == 'C':
					return 'Khá'
				elif obj[8] == 'B':
					return 'Giỏi'
				elif obj[8] == 'A':
					return 'Giỏi'
				else: return 'Giỏi'
			else: return 'Giỏi'
		elif obj[11] == '0.2':
			return 'Chưa Xếp Loại'
		else: return 'Khá'
	elif obj[16] == 'C':
		# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 178, "metric_value": 1.4112, "depth": 2}
		if obj[0] == 'B':
			# {"feature": "X\u00e1c su\u1ea5t th\u1ed1ng k\u00ea", "instances": 79, "metric_value": 1.2765, "depth": 3}
			if obj[13] == 'C':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 26, "metric_value": 0.8404, "depth": 4}
				if obj[3] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'D':
						return 'Khá'
					elif obj[1] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'C':
						return 'Khá'
					elif obj[1] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[3] == 'C':
					return 'Khá'
				elif obj[3] == 'B':
					# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[17] == 'B':
						return 'Khá'
					elif obj[17] == 'A':
						return 'Khá'
					elif obj[17] == 'D':
						return 'Khá'
					elif obj[17] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[3] == 'D':
					return 'Khá'
				elif obj[3] == 'F':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[13] == 'B':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 24, "metric_value": 1.4138, "depth": 4}
				if obj[17] == 'B':
					# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 15, "metric_value": 1.231, "depth": 5}
					if obj[6] == 'B':
						return 'Khá'
					elif obj[6] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[6] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[17] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[2] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'A':
						return 'Giỏi'
					else: return 'Chưa Xếp Loại'
				elif obj[17] == 'C':
					return 'Chưa Xếp Loại'
				elif obj[17] == 'D':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'C':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[13] == 'D':
				# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 20, "metric_value": 1.2345, "depth": 4}
				if obj[6] == 'D':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[1] == 'B':
						return 'Khá'
					elif obj[1] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[6] == 'C':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[10] == 'C':
						return 'Khá'
					elif obj[10] == 'B':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[6] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[6] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[13] == 'A':
				# {"feature": "C\u00f4ng ngh\u1ec7 Java", "instances": 6, "metric_value": 1.2516, "depth": 4}
				if obj[15] == 'A':
					return 'Chưa Xếp Loại'
				elif obj[15] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 1.585, "depth": 5}
					if obj[2] == 'A':
						return 'Khá'
					elif obj[2] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'B':
						return 'Giỏi'
					else: return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[13] == 'F':
				return 'Chưa Xếp Loại'
			else: return 'Khá'
		elif obj[0] == 'C':
			# {"feature": "C\u00f4ng ngh\u1ec7 Java", "instances": 49, "metric_value": 1.1184, "depth": 3}
			if obj[15] == 'A':
				# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[8] == 'C':
					# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[17] == 'B':
						return 'Khá'
					elif obj[17] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[17] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[8] == 'B':
					# {"feature": "To\u00e1n r\u1eddi r\u1ea1c", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[9] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[9] == 'D':
						return 'Khá'
					elif obj[9] == 'B':
						return 'Khá'
					else: return 'Khá'
				elif obj[8] == 'D':
					return 'Khá'
				elif obj[8] == 'A':
					return 'Khá'
				elif obj[8] == 'F':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[15] == 'B':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'B':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[10] == 'C':
						return 'Khá'
					elif obj[10] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[3] == 'C':
					return 'Khá'
				elif obj[3] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'C':
						return 'Khá'
					elif obj[2] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[3] == 'D':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[15] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 5, "metric_value": 1.5219, "depth": 4}
				if obj[2] == 'C':
					return 'Khá'
				elif obj[2] == 'B':
					return 'Chưa Xếp Loại'
				elif obj[2] == 'D':
					return 'Trung bình'
				else: return 'Khá'
			elif obj[15] == 'D':
				return 'Chưa Xếp Loại'
			elif obj[15] == '0':
				return 'Chưa Xếp Loại'
			else: return 'Khá'
		elif obj[0] == 'D':
			# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 31, "metric_value": 1.4725, "depth": 3}
			if obj[10] == 'C':
				# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 16, "metric_value": 1.2988, "depth": 4}
				if obj[1] == 'C':
					# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 1", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[7] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[7] == 'B':
						return 'Khá'
					elif obj[7] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[7] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[1] == 'D':
					# {"feature": "To\u00e1n r\u1eddi r\u1ea1c", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[9] == 'D':
						return 'Trung bình'
					elif obj[9] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[1] == 'B':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[10] == 'D':
				# {"feature": "X\u00e1c su\u1ea5t th\u1ed1ng k\u00ea", "instances": 11, "metric_value": 1.5395, "depth": 4}
				if obj[13] == 'B':
					# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[11] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[11] == 'B':
						return 'Khá'
					elif obj[11] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[13] == 'C':
					# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11] == 'C':
						return 'Trung bình'
					elif obj[11] == 'D':
						return 'Khá'
					else: return 'Trung bình'
				elif obj[13] == 'A':
					return 'Khá'
				elif obj[13] == 'D':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'B':
						return 'Trung bình'
					else: return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[10] == 'B':
				return 'Khá'
			elif obj[10] == 'A':
				return 'Chưa Xếp Loại'
			else: return 'Chưa Xếp Loại'
		elif obj[0] == 'A':
			# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 19, "metric_value": 1.3838, "depth": 3}
			if obj[12] == 'B':
				# {"feature": "C\u00f4ng ngh\u1ec7 Java", "instances": 9, "metric_value": 1.2244, "depth": 4}
				if obj[15] == 'A':
					# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[8] == 'C':
						return 'Khá'
					elif obj[8] == 'B':
						return 'Giỏi'
					elif obj[8] == 'A':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[15] == 'B':
					return 'Chưa Xếp Loại'
				elif obj[15] == 'C':
					return 'Khá'
				else: return 'Khá'
			elif obj[12] == 'D':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[17] == 'B':
					return 'Khá'
				elif obj[17] == 'F':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[12] == 'A':
				return 'Giỏi'
			elif obj[12] == 'F':
				return 'Chưa Xếp Loại'
			elif obj[12] == 'C':
				return 'Khá'
			else: return 'Khá'
		else: return 'Khá'
	elif obj[16] == 'A':
		# {"feature": "H\u1ec7 \u0111i\u1ec1u h\u00e0nh", "instances": 107, "metric_value": 1.7207, "depth": 2}
		if obj[14] == 'A':
			# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 64, "metric_value": 1.6959, "depth": 3}
			if obj[12] == 'A':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 41, "metric_value": 1.2102, "depth": 4}
				if obj[17] == 'A':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 36, "metric_value": 1.2516, "depth": 5}
					if obj[10] == 'A':
						return 'Xuất sắc'
					elif obj[10] == 'B':
						return 'Giỏi'
					elif obj[10] == 'C':
						return 'Giỏi'
					elif obj[10] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[17] == 'B':
					return 'Giỏi'
				else: return 'Giỏi'
			elif obj[12] == 'B':
				# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 17, "metric_value": 1.7131, "depth": 4}
				if obj[6] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[1] == 'B':
						return 'Giỏi'
					elif obj[1] == 'C':
						return 'Giỏi'
					elif obj[1] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[6] == 'B':
					# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 6, "metric_value": 1.4591, "depth": 5}
					if obj[8] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[8] == 'C':
						return 'Giỏi'
					elif obj[8] == 'A':
						return 'Giỏi'
					else: return 'Chưa Xếp Loại'
				elif obj[6] == 'D':
					return 'Khá'
				elif obj[6] == 'C':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'A':
						return 'Xuất sắc'
					elif obj[0] == 'B':
						return 'Giỏi'
					else: return 'Xuất sắc'
				else: return 'Giỏi'
			elif obj[12] == 'C':
				# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 1", "instances": 6, "metric_value": 1.4591, "depth": 4}
				if obj[7] == 'B':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4] == 'C':
						return 'Khá'
					elif obj[4] == 'A':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[7] == 'A':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			else: return 'Giỏi'
		elif obj[14] == 'B':
			# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 27, "metric_value": 1.1171, "depth": 3}
			if obj[3] == 'A':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 19, "metric_value": 0.7742, "depth": 4}
				if obj[0] == 'B':
					return 'Giỏi'
				elif obj[0] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1] == 'A':
						return 'Giỏi'
					elif obj[1] == 'D':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[0] == 'C':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'D':
						return 'Khá'
					elif obj[1] == 'A':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[0] == 'D':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'B':
						return 'Khá'
					elif obj[1] == 'C':
						return 'Giỏi'
					else: return 'Khá'
				else: return 'Giỏi'
			elif obj[3] == 'C':
				# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 6, "metric_value": 1.4591, "depth": 4}
				if obj[8] == 'C':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'B':
						return 'Khá'
					else: return 'Khá'
				elif obj[8] == 'A':
					return 'Giỏi'
				else: return 'Khá'
			elif obj[3] == 'D':
				return 'Khá'
			elif obj[3] == 'B':
				return 'Giỏi'
			else: return 'Giỏi'
		elif obj[14] == 'C':
			# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 12, "metric_value": 1.325, "depth": 3}
			if obj[17] == 'B':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[5] == 'C':
					return 'Khá'
				elif obj[5] == 'B':
					return 'Khá'
				elif obj[5] == 'A':
					return 'Giỏi'
				elif obj[5] == 'D':
					return 'Giỏi'
				else: return 'Khá'
			elif obj[17] == 'A':
				# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[11] == 'B':
					return 'Giỏi'
				elif obj[11] == 'C':
					return 'Chưa Xếp Loại'
				else: return 'Giỏi'
			elif obj[17] == 'C':
				return 'Khá'
			else: return 'Khá'
		elif obj[14] == 'D':
			# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0] == 'B':
				return 'Khá'
			elif obj[0] == 'A':
				return 'Chưa Xếp Loại'
			elif obj[0] == 'C':
				return 'Khá'
			else: return 'Khá'
		else: return 'Giỏi'
	elif obj[16] == 'D':
		# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 90, "metric_value": 1.349, "depth": 2}
		if obj[17] == 'B':
			# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 36, "metric_value": 0.9799, "depth": 3}
			if obj[11] == 'C':
				# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[12] == 'C':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[0] == 'B':
						return 'Khá'
					elif obj[0] == 'A':
						return 'Khá'
					elif obj[0] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[12] == 'D':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'C':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[12] == 'B':
					return 'Chưa Xếp Loại'
				elif obj[12] == 'A':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[11] == 'D':
				# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[1] == 'D':
					return 'Chưa Xếp Loại'
				elif obj[1] == 'C':
					return 'Khá'
				elif obj[1] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'C':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[11] == 'B':
				return 'Khá'
			elif obj[11] == '0':
				return 'Chưa Xếp Loại'
			elif obj[11] == '0.6':
				return 'Chưa Xếp Loại'
			elif obj[11] == 'F':
				return 'Chưa Xếp Loại'
			elif obj[11] == 'A':
				return 'Chưa Xếp Loại'
			else: return 'Chưa Xếp Loại'
		elif obj[17] == 'C':
			# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 28, "metric_value": 1.5, "depth": 3}
			if obj[10] == 'C':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 14, "metric_value": 1.4488, "depth": 4}
				if obj[4] == 'D':
					# {"feature": "H\u1ec7 \u0111i\u1ec1u h\u00e0nh", "instances": 7, "metric_value": 1.5567, "depth": 5}
					if obj[14] == 'C':
						return 'Khá'
					elif obj[14] == 'B':
						return 'Trung bình'
					elif obj[14] == 'D':
						return 'Trung bình'
					else: return 'Khá'
				elif obj[4] == 'F':
					return 'Chưa Xếp Loại'
				elif obj[4] == 'B':
					return 'Khá'
				elif obj[4] == 'A':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'C':
						return 'Khá'
					elif obj[0] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[4] == 'C':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[10] == 'D':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'C':
					# {"feature": "H\u1ec7 \u0111i\u1ec1u h\u00e0nh", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[14] == 'D':
						return 'Trung bình'
					elif obj[14] == 'C':
						return 'Trung bình'
					else: return 'Trung bình'
				elif obj[0] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Trung bình'
			elif obj[10] == 'B':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 5, "metric_value": 1.371, "depth": 4}
				if obj[4] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[4] == 'C':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[10] == '0':
				return 'Chưa Xếp Loại'
			else: return 'Chưa Xếp Loại'
		elif obj[17] == 'D':
			# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 16, "metric_value": 1.4197, "depth": 3}
			if obj[11] == 'D':
				# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 1", "instances": 11, "metric_value": 1.0958, "depth": 4}
				if obj[7] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[5] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'D':
						return 'Khá'
					elif obj[5] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'F':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[7] == 'D':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'C':
						return 'Trung bình'
					elif obj[3] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Trung bình'
				elif obj[7] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[11] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2] == 'D':
					return 'Trung bình'
				elif obj[2] == 'C':
					return 'Khá'
				else: return 'Trung bình'
			elif obj[11] == 'F':
				return 'Chưa Xếp Loại'
			elif obj[11] == 'B':
				return 'Khá'
			else: return 'Chưa Xếp Loại'
		elif obj[17] == 'A':
			# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[11] == 'D':
				return 'Chưa Xếp Loại'
			elif obj[11] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2] == 'C':
					return 'Khá'
				elif obj[2] == 'A':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			else: return 'Chưa Xếp Loại'
		elif obj[17] == 'F':
			return 'Chưa Xếp Loại'
		else: return 'Chưa Xếp Loại'
	elif obj[16] == 'F':
		return 'Chưa Xếp Loại'
	elif obj[16] == '0':
		return 'Chưa Xếp Loại'
	else: return 'Khá'
